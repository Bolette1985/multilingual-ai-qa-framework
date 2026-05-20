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
multilingual-ai-qa-framework/
├── src/
├── prompts/
├── results/
├── reports/