import os
import pandas as pd
import matplotlib.pyplot as plt

# =========================
# LOAD DATA
# =========================

INPUT_FILE = "results/output.csv"
OUTPUT_DIR = "reports"

os.makedirs(OUTPUT_DIR, exist_ok=True)

df = pd.read_csv(INPUT_FILE)

if df.empty:
    raise ValueError("No data found in output.csv")

# =========================
# METRICS
# =========================

accuracy = df["passed"].mean()
category_scores = df.groupby("category")["score"].mean()
language_scores = df.groupby("language")["score"].mean()

# =========================
# 1. CATEGORY CHART
# =========================

plt.figure()
category_scores.plot(kind="bar")
plt.title("Accuracy by Category")
plt.ylabel("Score")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/accuracy_by_category.png")
plt.close()

# =========================
# 2. LANGUAGE CHART
# =========================

plt.figure()
language_scores.plot(kind="bar")
plt.title("Accuracy by Language")
plt.ylabel("Score")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/accuracy_by_language.png")
plt.close()

# =========================
# 3. SCORE DISTRIBUTION
# =========================

plt.figure()
df["score"].value_counts().sort_index().plot(kind="bar")
plt.title("Score Distribution")
plt.xlabel("Score")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/score_distribution.png")
plt.close()

# =========================
# MARKDOWN REPORT
# =========================

report = f"""
# 📊 AI Evaluation Report

## Overall Performance
- Accuracy: {accuracy:.2%}
- Total Tests: {len(df)}

## Category Performance
{category_scores.to_string()}

## Language Performance
{language_scores.to_string()}

## Files Generated
- accuracy_by_category.png
- accuracy_by_language.png
- score_distribution.png
"""

with open(f"{OUTPUT_DIR}/report.md", "w", encoding="utf-8") as f:
    f.write(report)

print("✅ Report generated in /reports")