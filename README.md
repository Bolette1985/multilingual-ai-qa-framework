# 🌍 Multilingual LLM & Agentic AI Evaluation Framework

A modular, config-driven Python framework for evaluating Large Language Models (LLMs) across multilingual, reasoning, and hallucination-sensitive tasks.

---

## 🚀 Overview

This project is an AI Quality Engineering framework designed to benchmark LLM behavior in structured evaluation settings.

It supports reproducible testing of:
- Multilingual performance (English + Danish)
- Hallucination susceptibility
- Reasoning under synthetic and hard prompts
- Structured evaluation pipelines for LLM outputs

The system is built with a focus on **reproducibility, modularity, and experiment control**, similar to real-world AI QA workflows.

---

## 🧠 Key Design Principles

- 🔁 Reproducible experiments (fixed random seed)
- ⚙️ Config-driven execution (JSON-based control)
- 🧩 Modular architecture (separated pipeline components)
- 📊 Structured evaluation outputs
- 🧪 Synthetic dataset generation for controlled testing

---

## 🏗️ Architecture

```text
multilingual-ai-qa-framework/
│
├── config.json                # Experiment configuration
├── prompts/                   # Generated datasets
├── results/                   # Evaluation outputs (CSV)
├── reports/                   # Metrics and visual reports
│
├── src/
│   ├── main.py                # Pipeline orchestrator
│   ├── evaluator.py          # LLM evaluation logic
│   ├── dataset_loader.py     # Loads latest dataset
│   ├── result_handler.py     # Saves structured outputs
│   ├── metrics.py            # Summary statistics
│
└── README.md
```