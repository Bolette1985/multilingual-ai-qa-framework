# 🌍 Multilingual AI QA Evaluation Framework

A lightweight Python framework for evaluating Large Language Models (LLMs) on multilingual performance, hallucination resistance, and factual accuracy using automated test prompts.

---

## 🚀 What this project does

This framework automatically:

- Generates synthetic evaluation prompts (English + Danish)
- Tests LLM responses using Google Gemini API
- Scores outputs for correctness and hallucination resistance
- Saves structured results as CSV
- Generates performance reports with visual charts

---

## 🧠 Key Features

### 📌 Prompt Generation
- Hallucination-based test cases
- Hard reasoning prompts
- Multilingual support (English + Danish)
- Configurable dataset size

### 🤖 Evaluation Engine
- Uses Google Gemini (`gemini-2.5-flash`)
- Automatic retry handling for rate limits
- Category-based scoring system
- Safe-word hallucination detection

### 📊 Reporting System
- Accuracy per category
- Accuracy per language
- Score distribution analysis
- Auto-generated charts (matplotlib)
- Markdown summary report

---

## 📁 Project Structure

```text
multilingual-ai-qa-framework/
├── src/
│   ├── main.py
│   ├── evaluator.py
│   ├── prompt_generator.py
│   └── report_generator.py
│
├── prompts/
│   └── generated_*.json
│
├── results/
│   └── output.csv
│
├── reports/
│   ├── report.md
│   ├── accuracy_by_category.png
│   ├── accuracy_by_language.png
│   └── score_distribution.png
│
├── .gitignore
├── README.md
└── requirements.txt
```
