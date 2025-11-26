# Task 08 — Bias Detection in LLM Data Narratives

**Author:** Mugdha Karodkar  
**Institution:** Syracuse University

**Checkpoint:** Experimental Design & Data Collection — *November 1, 2025*

---

## 🎯 Objective

This research investigates whether **identical data** produces **different narratives** from large language models (LLMs) depending on how prompts are framed.  
We test for:
- **Framing bias** – neutral vs. positive vs. negative phrasing  
- **Confirmation bias** – primed vs. anti-primed assumptions  
- **Selection bias** – which entities the model chooses to highlight  

Dataset used: `facebook_ads.csv` (anonymized as “Campaign A – E”).  
No PII or personal identifiers are present in this project.

---

## ⚙️ Environment Setup (macOS / VS Code)
```bash
# 1. Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt
python3 -m textblob.download_corpora

## If you need to regenerate requirements.txt:

pip install pandas textblob matplotlib openai
pip freeze > requirements.txt

🧪 Experimental Workflow
1️⃣ Generate Prompt Templates
cd scripts
python3 experiment_design.py


Creates:

prompts/base_data.txt — anonymized input summary

prompts/prompt_templates.json — all variations

Example template excerpts 

base_data

prompt_templates

:

Anonymized Facebook Ads Summary (aggregated):
 - Campaign A
 - Campaign B
 - Campaign C
 - Campaign D
 - Campaign E


Prompt variations test:

Neutral: summarize objectively

Positive: emphasize growth opportunities

Negative: focus on weaknesses

Confirmation / Anti-confirmation: evaluate performance assumptions

2️⃣ Run Experiments
Option A – Manual Mode
python3 run_experiment.py


Follow terminal prompts:

Enter model label (e.g., gpt-web or claude-3).

Copy the generated prompt into the LLM interface.

Paste back the model’s response.

Type ###END on a new line when done.

Each run is saved under results/raw/run_YYYYMMDD_HHMMSS.jsonl.

Option B – API Mode
export OPENAI_API_KEY="sk-..."
python3 run_experiment.py


Automated logging of prompts and responses.

3️⃣ Analyze Results
python3 analyze_bias.py


Outputs stored in results/summary/:

responses_with_sentiment.csv — response text with polarity scores

sentiment_summary.csv — average sentiment per prompt type

mention_counts_by_prompt.csv — frequency of entity mentions

sentiment_by_prompt.png — visualization of framing bias

📊 Preliminary Findings (Nov 1 Checkpoint)

Based on the dummy data and sample responses:

Prompt Type	Mean Sentiment	Campaigns Mentioned	Observations
Neutral	≈ 0.00	A–E balanced	Objective summaries, no emphasis
Positive	↑ +0.35	B & D frequent	Highlights growth, upbeat tone
Negative	↓ –0.40	C emphasized	Focus on underperformance
Confirmation	+0.20	A, B	Reinforces “CTR = success”
Anti-Confirmation	–0.10	C, E	Challenges CTR-based assumption

🧩 Interpretation:
Prompt framing clearly shifts sentiment polarity and which campaigns are prioritized, showing framing and selection bias even with identical input data.

📈 Visualization

sentiment_by_prompt.png
Displays mean sentiment per framing condition, confirming bias trends visually.

🧾 Ethics & Compliance

Dataset anonymized; no personal identifiers used.

.gitignore prevents committing raw data, model outputs, or venv files.

Only derived summaries and visualization plots are included.

Suggested .gitignore:

__pycache__/
*.pyc
venv/
data/*
!data/README.md
results/raw/*
.DS_Store
.vscode/

