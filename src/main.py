import os
import json
import glob
import pandas as pd
from dotenv import load_dotenv
from google import genai
from evaluator import evaluate_prompt

# =========================
# INIT
# =========================

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("❌ GEMINI_API_KEY not found in .env file")

client = genai.Client(api_key=api_key)

print("🔥 AI Evaluation Runner Started")


# =========================
# LOAD LATEST DATASET
# =========================

prompt_files = glob.glob("prompts/generated_*.json")

if not prompt_files:
    raise FileNotFoundError("❌ No generated prompt files found")

PROMPT_FILE = max(prompt_files, key=os.path.getctime)

print(f"📂 Using dataset: {PROMPT_FILE}")


with open(PROMPT_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

results = []


# =========================
# RUN EVALUATION
# =========================

for category, prompts in data.items():

    print(f"\n📂 Running category: {category}")

    for item in prompts:

        result = evaluate_prompt(client, item, category)
        results.append(result)

        print(f"✔ Prompt {item['id']} completed")


# =========================
# SAVE RESULTS
# =========================

os.makedirs("results", exist_ok=True)

df = pd.DataFrame(results)

output_path = "results/output.csv"
df.to_csv(output_path, index=False)


# =========================
# SUMMARY
# =========================

if len(df) == 0:
    print("❌ No results generated - check API or dataset")
    exit()

accuracy = df["passed"].mean()
category_scores = df.groupby("category")["score"].mean()

print("\n==============================")
print("✅ EVALUATION COMPLETE")
print("==============================")
print(f"📊 Total Tests: {len(df)}")
print(f"📈 Accuracy: {accuracy:.2%}")
print(f"💾 Results saved to: {output_path}")
print("\n📊 Category Performance")
print((category_scores * 100).round(2).astype(str) + "%")
print("==============================")