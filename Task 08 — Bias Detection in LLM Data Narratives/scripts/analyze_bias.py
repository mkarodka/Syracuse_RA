import re
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from textblob import TextBlob

# Paths
RAW_DIR = Path("../results/raw")
SUM_DIR = Path("../results/summary")
SUM_DIR.mkdir(parents=True, exist_ok=True)

# Load the most recent results file
files = sorted(RAW_DIR.glob("run_*.jsonl"))
assert files, "No results found in results/raw/*.jsonl"
data = pd.read_json(files[-1], lines=True)

# --- Sentiment analysis ---
data["sentiment"] = data["response_text"].fillna("").apply(lambda x: TextBlob(x).sentiment.polarity)
sent_summary = data.groupby("prompt_id")["sentiment"].agg(["mean", "std", "count"]).sort_values("mean")

# --- Mentions (detect which campaigns are named) ---
def mentions(text):
    return re.findall(r"\bCampaign\s+[A-E]\b", text or "")

exp_rows = []
for _, r in data.iterrows():
    for m in set(mentions(r["response_text"])):
        exp_rows.append({
            "prompt_id": r["prompt_id"],
            "model": r["model"],
            "campaign": m,
            "replicate": r["replicate"]
        })

mention_df = pd.DataFrame(exp_rows)
mention_pivot = (
    mention_df.pivot_table(
        index="prompt_id",
        columns="campaign",
        values="replicate",
        aggfunc="count",
        fill_value=0
    )
    if not mention_df.empty
    else pd.DataFrame()
)

# --- Save outputs ---
out1 = SUM_DIR / "responses_with_sentiment.csv"
out2 = SUM_DIR / "sentiment_summary.csv"
out3 = SUM_DIR / "mention_counts_by_prompt.csv"

data.to_csv(out1, index=False)
sent_summary.to_csv(out2)
if not mention_pivot.empty:
    mention_pivot.to_csv(out3)

# --- Plotting ---
plt.figure()
sent_summary["mean"].plot(kind="bar", title="Average Sentiment by Prompt")
plt.ylabel("Polarity (-1..1)")
plt.tight_layout()
plt.savefig(SUM_DIR / "sentiment_by_prompt.png", dpi=160)

# --- Summary output ---
print("✅ Wrote the following files:")
print(" -", out1)
print(" -", out2)
if not mention_pivot.empty:
    print(" -", out3)
print(" -", SUM_DIR / "sentiment_by_prompt.png")
