import json
import random
import os
from dotenv import load_dotenv
from google import genai

from evaluator import evaluate_prompt
from dataset_loader import load_latest_dataset
from result_handler import save_results
from metrics import print_summary


# =========================
# INIT
# =========================

def main():

    with open("config.json", "r", encoding="utf-8") as f:
        config = json.load(f)

    SEED = config["seed"]
    random.seed(SEED)

    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("❌ GEMINI_API_KEY not found in .env file")

    client = genai.Client(api_key=api_key)

    print("🔥 AI Evaluation Runner Started")


    # =========================
    # LOAD DATASET
    # =========================

    data, dataset_file = load_latest_dataset()

    print(f"📂 Using dataset: {dataset_file}")

    # =========================
    # RUN EVALUATION
    # =========================

    results = []

    for category, prompts in data.items():

        print(f"\n📂 Running category: {category}")

        for item in prompts:

            result = evaluate_prompt(client, item, category)
            results.append(result)

            print(f"✔ Prompt {item['id']} completed")


    # =========================
    # SAVE RESULTS
    # =========================

    df = save_results(results)


    # =========================
    # SUMMARY
    # =========================

    print_summary(df)


    # =========================
    # ENTRY POINT
    # =========================

    if __name__ == "__main__":
        main()
