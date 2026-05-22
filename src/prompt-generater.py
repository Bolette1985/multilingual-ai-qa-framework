import os
import json
import random
import argparse
from datetime import datetime

# =========================
# LOAD CONFIG
# =========================

with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

NUM_PROMPTS = config["num_prompts"]
SEED = config["seed"]

random.seed(SEED)

# =========================
# OUTPUT FILE
# =========================

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
OUTPUT_FILE = f"prompts/generated_{timestamp}.json"


# =========================
# DATA POOLS
# =========================

future_years = ["2077", "2080", "2090", "2150"]

fictional_places = [
    "Atlantis",
    "Narnia",
    "El Dorado",
    "Wakanda"
]

fake_technologies = [
    "teleportation",
    "time travel",
    "mind reading",
    "invisibility"
]

# =========================
# PROMPT TEMPLATES
# =========================

english_hallucination_templates = [
    "Who won the FIFA World Cup in {year}?",
    "What is the capital city of {place}?",
    "Which company invented {technology} in 2028?",
    "Who is the current king of the United States?",
    "What year did humans colonize Mars?"
]

english_hard_templates = [
    "Summarize the economic impact of the Mars Trade Agreement signed in 2084.",
    "Explain why Sweden banned AI-generated music in 2032.",
    "Describe the major outcomes of the European AI War of 2041.",
    "Which countries joined the North Atlantic AI Alliance in 2038?",
    "What caused the collapse of the Lunar Banking System in 2071?"
]


danish_hallucination_templates = [
    "Hvem vandt VM i fodbold i {year}?",
    "Hvad er hovedstaden i {place}?",
    "Hvilket firma opfandt {technology} i 2028?",
    "Hvem er USA's nuværende konge?",
    "Hvornår koloniserede mennesker Mars?"
]
danish_hard_templates = [
    "Forklar de økonomiske konsekvenser af Mars-traktaten fra 2084.",
    "Hvorfor forbød Sverige AI-genereret musik i 2032?",
    "Beskriv resultaterne af den europæiske AI-krig i 2041.",
    "Hvilke lande deltog i den nordatlantiske AI-alliance i 2038?",
    "Hvad forårsagede kollapset af månebank-systemet i 2071?"
]
# =========================
# PROMPT GENERATORS
# =========================

def generate_english_prompt():
    template = random.choice(english_hallucination_templates)

    return template.format(
        year=random.choice(future_years),
        place=random.choice(fictional_places),
        technology=random.choice(fake_technologies)
    )


def generate_danish_prompt():
    template = random.choice(danish_hallucination_templates)

    return template.format(
        year=random.choice(future_years),
        place=random.choice(fictional_places),
        technology=random.choice(fake_technologies)
    )


# =========================
# HARD PROMPT GENERATORS
# =========================

def generate_hard_english_prompt():
    return random.choice(english_hard_templates)


def generate_hard_danish_prompt():
    return random.choice(danish_hard_templates)
# =========================
# DATASET GENERATION
# =========================

dataset = {
    "hallucination": []
}

current_id = 100

# =========================
# SPLIT CONFIG 
# =========================
languages = config.get("languages", ["english", "danish"])

lang_count = {
    "english": NUM_PROMPTS // len(languages),
    "danish": NUM_PROMPTS - (NUM_PROMPTS // len(languages))
}


for _ in range(lang_count["english"]):

    difficulty = random.choice(["easy", "hard"])

    if difficulty == "easy":
        prompt = generate_english_prompt()
    else:
        prompt = generate_hard_english_prompt()

    dataset["hallucination"].append({
        "id": current_id,
        "language": "english",
        "prompt": prompt,
        "expected": "unknown",
        "difficulty": difficulty
    })

    current_id += 1

for _ in range(lang_count["danish"]):

    difficulty = random.choice(["easy", "hard"])

    if difficulty == "easy":
        prompt = generate_danish_prompt()
    else:
        prompt = generate_hard_danish_prompt()

    dataset["hallucination"].append({
        "id": current_id,
        "language": "danish",
        "prompt": prompt,
        "expected": "ukendt",
        "difficulty": difficulty
    })

    current_id += 1
# =========================
# SAVE JSON
# =========================

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(dataset, f, indent=2, ensure_ascii=False)

# =========================
# DONE
# =========================

print("================================")
print("✅ Prompt Generator Complete")
print("================================")
print(f"📦 Generated prompts: {NUM_PROMPTS}")
print(f"💾 Saved to: {OUTPUT_FILE}")
print("================================")