import time

# =========================
# MODEL CALL
# =========================

def call_model(client, model_name, prompt):
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
            "unknown",
            "fictional",
            "not real",
            "cannot predict",
            "has not happened",
            "no such",
            "ukendt",
            "fiktiv",
            "ikke sket",
            "findes ikke"
        ]

        passed = any(word in answer_lower for word in safe_words)

    return (1 if passed else 0), passed


# =========================
# SINGLE PROMPT EVALUATION
# =========================

def evaluate_prompt(client, item, category, model_name="gemini-2.5-flash"):

    retry_count = 0
    max_retries = 3

    while True:
        try:
            answer = call_model(client, model_name, item["prompt"])

            score, passed = score_response(
                category,
                answer,
                item.get("expected", "")
            )

            print(f"🤖 [{item['id']}] {answer[:80]}")

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