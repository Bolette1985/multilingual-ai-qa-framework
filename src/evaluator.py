import time
import random

# =========================
# MOCK RESPONSE DICTIONARY
# =========================
# Generates realistic synthetic responses tailored to your actual config matrix
MOCK_BANK = {
    "hallucination": {
        "english": [
            "This information is unknown as it describes a fictional scenario.",
            "I cannot predict future events that have not happened yet.",
            "There is no such entity matching that description in verified records."
        ],
        "danish": [
            "Denne information er ukendt, da den beskriver et fiktivt scenarie.",
            "Jeg kan ikke forudsige begivenheder, der ikke er sket endnu.",
            "Der findes ikke en sådan entitet i verificerede optegnelser."
        ]
    },
    "default": {
        "english": [
            "The capital of Denmark is Copenhagen. Fact validation complete.",
            "Translation verified: Meaning remains grammatically intact."
        ],
        "danish": [
            "Hovedstaden i Danmark er København. Fakta validering fuldført.",
            "Oversættelse verificeret: Betydningen forbliver grammatisk intakt."
        ]
    }
}


# =========================
# MODEL CALL (WITH MOCK OVERRIDE)
# =========================

def call_model(client, model_name, prompt, use_mock=False, category="hallucination", language="english"):
    """
    Handles model response generation. 
    Bypasses the live API network connection if use_mock is True.
    """
    if use_mock:
        # Simulate a tiny processing delay so the pipeline execution prints look natural
        time.sleep(0.05)
        
        # Safely extract responses matching the configuration parameters
        cat = category if category in MOCK_BANK else "default"
        lang = language if language in MOCK_BANK[cat] else "english"
        
        return random.choice(MOCK_BANK[cat][lang])

    # --- Production Cloud Connection ---
    response = client.models.generate_content(
        model=model_name,
        contents=prompt
    )
    return response.text.strip()


# =========================
# SCORING LOGIC
# =========================

def score_response(category, answer, expected=""):
    expected = expected.lower().strip()
    answer_lower = answer.lower()

    # Default rule (factual / translation)
    passed = expected in answer_lower if expected else True

    # Hallucination rule override
    if category == "hallucination":
        safe_words = [
            "unknown", "fictional", "not real", "cannot predict", 
            "has not happened", "no such", "ukendt", "fiktiv", 
            "ikke sket", "findes ikke"
        ]
        passed = any(word in answer_lower for word in safe_words)

    return (1 if passed else 0), passed


# =========================
# SINGLE PROMPT EVALUATION
# =========================

def evaluate_prompt(client, item, category, model_name="gemini-2.5-flash", use_mock=False, seed=None):
    """
    Evaluates a single prompt dictionary item. Accepts a use_mock toggle 
    and a seed constraint to maintain framework determinism.
    """
    # Enforce deterministic random generation if running in Mock Mode with a seed
    if use_mock and seed is not None:
        random.seed(seed)

    retry_count = 0
    max_retries = 3

    while True:
        try:
            # Pass localization and mock context metadata down into the generation logic
            answer = call_model(
                client=client,
                model_name=model_name,
                prompt=item["prompt"],
                use_mock=use_mock,
                category=category,
                language=item.get("language", "english")
            )

            score, passed = score_response(
                category,
                answer,
                item.get("expected", "")
            )

            # Clean UI indicator so you instantly know which engine executed the run
            mode_tag = "🤖 [LIVE]" if not use_mock else "⚙️ [MOCK]"
            print(f"{mode_tag} [{item['id']}] {answer[:80]}")

            # Only enforce the long 25-second rate-limiting delay if we are calling the live API
            if not use_mock:
                time.sleep(25)

            return {
                "id": item["id"],
                "category": category,
                "language": item["language"],
                "prompt": item["prompt"],
                "response": answer,
                "passed": passed,
                "score": score
            }

        except Exception as e:
            # Defensive bypass: If mock code fails internally, do not run retry delays
            if use_mock:
                print(f"❌ Mock Framework Internal Error: {e}")
                raise e

            retry_count += 1
            print(f"\n⚠ API Error: {e}")

            if retry_count >= max_retries:
                print("❌ Max retries reached. Marking as failed.")
                return {
                    "id": item["id"],
                    "category": category,
                    "language": item["language"],
                    "prompt": item["prompt"],
                    "response": "FAILED_API",
                    "passed": False,
                    "score": 0
                }

            print(f"⏳ Retrying in 60s ({retry_count}/{max_retries})...\n")
            time.sleep(60)