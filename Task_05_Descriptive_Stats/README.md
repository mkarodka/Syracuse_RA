# Task_05_Descriptive_Stats

This project explores descriptive statistics using Syracuse University Women's Basketball dataset, combined with prompt engineering to interact with a Large Language Model (LLM) for question answering and insight generation.

## 📌 Objective

To analyze a small, real-world dataset using Python and challenge a Large Language Model (ChatGPT) with natural language questions about the data. The goal is to assess the LLM’s reasoning capabilities and support its responses with descriptive statistics and visualizations.

## 🗂️ Project Structure

```
task05-womens-basketball/
├── generate_stats.py                # Script to compute basic statistics
├── generate_visuals.py             # Script to generate visualizations
├── llm_prompts_and_responses.md    # Prompt engineering experiments with LLM
├── README.md                       # Project description and usage guide
├── subset.csv                      # Subset data used for analysis (NOT uploaded to GitHub)
├── WBBStatsFile01.csv              # Original dataset (NOT uploaded to GitHub)
├── *.png                           # Visualizations generated
└── venv/                           # Local virtual environment (not tracked)
```

## 📊 Visualizations

The following plots were generated from the dataset:

- `assists_vs_turnovers.png`
- `blocks_per_game_vs_teams.png`
- `wins_vs_teams.png`
- `free_throw_pct_vs_teams.png`
- `opponent_fg_pct_vs_teams.png`

These charts offer insights into team performance trends across key metrics.

## 🤖 Prompt Engineering with LLMs

Refer to [`llm_prompts_and_responses.md`](llm_prompts_and_responses.md) for:

- Natural language questions posed to ChatGPT
- Prompt refinements used to extract better answers
- Successes and limitations of LLM responses
- Evaluation of LLM accuracy based on computed stats

## 🧪 Methodology

1. **Data Analysis**:
   - Imported, cleaned, and explored the dataset (`generate_stats.py`)
   - Generated statistical summaries like totals and averages

2. **Visualization**:
   - Used `matplotlib` to create bar and scatter plots (`generate_visuals.py`)

3. **LLM Interaction**:
   - Asked questions like:
     - “How many games did this team play?”
     - “Who was the most consistent performer?”
     - “What should a coach focus on to win 2 more games next season?”

4. **Validation**:
   - LLM answers were validated against the actual dataset using the stats generated.

## 🔗 References

- [Original SU Women’s Basketball Stats](https://cuse.com/sports/2013/1/16/WLAX_0116134638)
- Syracuse RA Task 5 Document (attached separately)

## 💡 Future Work

- Try more complex LLMs (Claude, CoPilot) for richer interpretation
- Define custom performance metrics (e.g., “most improved player”)
- Attempt predictive modeling or trend forecasting
