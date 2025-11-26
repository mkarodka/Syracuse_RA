# Task 07 – Attempting an Actionable Report for Human Decision Makers

## 🎯 Objective

The goal of Task 7 was to move beyond pure descriptive statistics and prompt–response experimentation (Tasks 4–6) toward producing an **actionable report** targeted at human decision-makers. The emphasis was not solely on the end-product but rather on **documenting the process, workflow, and challenges** in bridging raw data/LLM outputs with decision-ready insights.

## 🧭 Workflow & Research Process

### Step 1: Reviewing Previous Tasks

* **Task 4 (Social Media Stats – 2024 U.S. Presidential Candidates):**

  * Focused on descriptive statistics from political ad/post datasets.
  * Explored data via Python (pure Python, Pandas, Polars) and visualization libraries.
  * Outputs: most frequent ad dates, top candidates, audience size trends, etc.
  * Limitation: Findings were **technical summaries** but not contextualized for decision makers (e.g., campaign managers, policy analysts).

* **Task 5 (Women’s Basketball Dataset + LLM):**

  * Combined descriptive stats with **prompt engineering** to test how an LLM interprets structured stats.
  * LLM correctly answered factual queries (e.g., highest wins, best assist-to-turnover ratio).
  * It also gave nuanced advice (e.g., defensive improvement based on blocks + opponent FG%).
  * Limitation: Responses were **accurate but fragmented** — not structured as a report.

* **Task 6 (Deep Fake Interview):**

  * Explored narrative transformation and **audience engagement through storytelling**.
  * Demonstrated that technical outputs can be **reframed into more accessible formats**.
  * Limitation: While engaging, it lacked integration with quantitative evidence.

### Step 2: Defining “Actionable Report”

For this task, I researched what makes a report “actionable”:

* Must be **audience-specific** (decision makers, not data scientists).
* Must **highlight implications, not just stats**.
* Must **recommend actions** based on findings.
* Should balance **quantitative evidence** (charts, stats) with **narrative clarity**.

### Step 3: Attempt to Build the Report

I attempted to create a **prototype actionable report** based on the Women’s Basketball dataset (Task 5), since it already had clean metrics and meaningful comparisons.

1. **Data-Driven Insights Extracted:**

   * *South Carolina*: Best defense → low opponent FG%, high blocks.
   * *Iowa & UConn*: Strong ball control → highest Assist-to-Turnover ratios.
   * *Gonzaga*: Best free-throw percentage → reliable under pressure.
   * *South Carolina*: Perfect season → evidence of multi-dimensional strength.

2. **Drafted Report Structure:**

   * **Executive Summary:** Key findings in plain language.
   * **Team Profiles:** One-sentence takeaways per top team.
   * **Recommendations:** What decision makers (e.g., coaches, analysts) should focus on:

     * Study South Carolina for defensive strategies.
     * Emphasize guard play and passing efficiency (Iowa, UConn).
     * Improve free-throw consistency to gain extra wins (Gonzaga benchmark).

3. **Challenges Encountered:**

   * LLM tended to **repeat descriptive stats** rather than synthesize action items.
   * Translating **data trends into coaching recommendations** required **human judgment + prompt refinement**.
   * Balancing **technical precision** with **accessible storytelling** was iterative.

### Step 4: Iterative Prompt Engineering

I experimented with prompts like:

* “Write a coaching strategy memo based on these stats.”
* “Summarize this dataset as if presenting to a sports analyst.”
* “Which 3 changes should a coach implement to increase wins?”

Findings:

* LLM could provide structured recommendations (e.g., focus on turnovers, defense, free throws).
* Quality improved when **context was provided first** (dataset + stats) before asking for actionable takeaways.

## 📌 Key Observations

* **Successes:**

  * LLM responses were accurate and often insightful when guided with context.
  * It was possible to extract actionable insights (defense focus, free throw improvements, turnover control).
  * The Deep Fake experiment (Task 6) highlighted storytelling as a valuable tool to **reframe technical data**.

* **Limitations:**

  * Reports lacked **quantified impact estimates** (e.g., “improving FT% by 5% → +2 wins”).
  * LLM often needed **human intervention** to avoid vague/general suggestions.
  * Translation from dataset → stats → insights → narrative required **multiple iterations**.

## 📝 Conclusion

Task 7 demonstrated that producing an **actionable report** is less about generating new stats and more about:

1. Structuring outputs for decision makers.
2. Refining LLM prompts to move from descriptive → prescriptive insights.
3. Documenting workflow attempts, including failures and iterations.

This task highlighted the gap between **data summaries** and **decision-ready recommendations**. While LLMs can accelerate interpretation, **human oversight is critical** for ensuring relevance, clarity, and actionability.

