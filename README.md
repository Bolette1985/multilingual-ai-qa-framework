# 🌍 Multilingual LLM & Agentic AI Evaluation Framework

A modular, configuration-driven Python testing framework engineered to benchmark Large Language Models (LLMs) and validate behavior across multilingual boundary constraints, deterministic reasoning paths, and hallucination vectors.

---

## 🚀 Overview

This framework is built for **AI Quality Engineering (AI QE)** and **LLMOps validation**. Moving past manual prompt "vibe-checks," it implements structured pipelines to programmatically run hard prompt testing and analyze model regressions.

### 🧪 Target Evaluation Capabilities
- **Multilingual Edge-Case Optimization:** Validating linguistic nuances, idioms, and structural accuracy across complex localized datasets (**English** and **Danish**).
- **Hallucination Mitigation:** Quantifying susceptibility to false premises and unverified assertions using deterministic string validation matching rules.
- **Reasoning Calibration:** Measuring model adherence to explicit context bounds using hard-prompt synthetic injection.
- **Cost-Efficient Isolation:** Fully independent simulation capabilities to bypass production cloud APIs during local pipeline testing.

---

## 🧠 Key Architecture & Design Principles

- **🔁 Enforced Determinism:** Leverages unified configuration seeds (`random.seed`) to ensure model datasets and local simulation runs are completely reproducible across test runs.
- **⚙️ Config-Driven Execution:** Orchestrates entire experiment parameters (dataset constraints, target language arrays, evaluation types) using a single externalized JSON control matrix (`config.json`).
- **🧩 Separation of Concerns:** Rigidly divides data orchestration, prompt generation, model client execution, and log handling into isolated, object-oriented software modules.
- **📊 Production-Ready Output Engineering:** Compiles execution metrics directly into structured `pandas` data pipelines to generate exportable verification logs and summary statistics.

---

## 🏗️ Project Architecture

```text
multilingual-ai-qa-framework/
│
├── config.json                # Centralized JSON experiment configuration
├── .env                       # Local execution environment variables (API Keys)
├── requirements.txt           # Python ecosystem dependencies
│
├── prompts/                   # Hardcoded inputs & dynamically generated datasets
│   ├── factual_questions.json
│   └── generated_prompts.json
│
├── results/                   # Evaluation artifacts & structured metric tracking (CSV)
│   └── output.csv             
│
├── src/                       # Core Framework Source
│   ├── main.py                # Pipeline orchestrator and entry-point
│   ├── evaluator.py           # LLM client execution interface, scoring rules & Mock logic
│   ├── dataset_loader.py      # Upstream dataset parsing and mutation handler
│   ├── result_handler.py      # Downstream pandas logging and file persistence
│   ├── prompt-generater.py    # Synthetic dataset creation pipeline
│   ├── report-generator.py    # Evaluation visualization and metric rendering
│   └── metrics.py             # Core pipeline telemetry and summary stats