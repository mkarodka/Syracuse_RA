import os, json, math, re
import pandas as pd
import numpy as np

DATA_PATH = os.path.join("..", "data", "facebook_ads.csv")
OUT_DIR = os.path.join("..", "prompts")
os.makedirs(OUT_DIR, exist_ok=True)

def coerce_numeric(series: pd.Series) -> pd.Series:
    # Turn things like "$1,234.50" or "12,345" into numbers
    return pd.to_numeric(
        series.astype(str)
              .str.replace(r"[\$,]", "", regex=True)
              .str.replace(r"\s+", "", regex=True)
              .str.replace(r"(NA|NaN|None)$", "", regex=True),
        errors="coerce"
    )

# --- 1) Load & normalize columns ---
df = pd.read_csv(DATA_PATH)
df.columns = [c.lower().strip().replace(" ", "_") for c in df.columns]
if df.empty:
    raise SystemExit("facebook_ads.csv appears empty.")

# Pick a campaign-like identifier
candidate_id_cols = [c for c in df.columns if any(k in c for k in ["campaign", "ad_id", "adname", "ad_name", "name", "id"])]
campaign_col = candidate_id_cols[0] if candidate_id_cols else df.columns[0]

# Split id vs metrics
metric_cols = [c for c in df.columns if c != campaign_col]

# Coerce non-id columns to numeric where possible
for c in metric_cols:
    df[c] = coerce_numeric(df[c])

# Keep id + any columns that became numeric
numeric_cols = [c for c in metric_cols if pd.api.types.is_numeric_dtype(df[c])]
keep = [campaign_col] + numeric_cols
df = df[keep].copy()

if not numeric_cols:
    raise SystemExit(
        "No numeric metric columns detected after coercion.\n"
        f"Detected columns: {list(df.columns)}\n"
        "Tip: Ensure your CSV has numeric metrics like impressions/clicks/spend/conversions, "
        "or remove currency symbols/commas from the raw data."
    )

# --- 2) Aggregate by campaign/ad id (sum) ---
grouped = df.groupby(campaign_col, dropna=False)[numeric_cols].sum(min_count=1).reset_index()

# --- 3) Derive common KPIs if possible ---
def safe_ratio(a, b):
    with np.errstate(divide="ignore", invalid="ignore"):
        res = np.where((b is not None) & (np.asarray(b) != 0), np.asarray(a) / np.asarray(b), np.nan)
    return res

# Heuristic names
impr_col = next((c for c in grouped.columns if c == "impressions"), None)
clicks_col = next((c for c in grouped.columns if c == "clicks"), None)
spend_col = next((c for c in grouped.columns if c == "spend"), None)
conv_col = next((c for c in grouped.columns if c == "conversions"), None)

grouped["ctr"] = safe_ratio(grouped[clicks_col], grouped[impr_col]) if (impr_col and clicks_col) else np.nan
grouped["cpc"] = safe_ratio(grouped[spend_col], grouped[clicks_col]) if (spend_col and clicks_col) else np.nan
grouped["cvr"] = safe_ratio(grouped[conv_col], grouped[clicks_col]) if (conv_col and clicks_col) else np.nan
grouped["cpa"] = safe_ratio(grouped[spend_col], grouped[conv_col]) if (spend_col and conv_col) else np.nan

# --- 4) Sort and pick top 5 for the prompt block ---
sort_order = [c for c in ["impressions", "clicks", "conversions", "spend"] if c in grouped.columns]
grouped = grouped.sort_values(by=sort_order if sort_order else [numeric_cols[0]], ascending=False, kind="stable")
top = grouped.head(5).copy()

def fmt_money(x):
    try:
        fx = float(x)
        return f"${round(fx, 2)}"
    except Exception:
        return "NA"

def fmt_pct(x):
    try:
        fx = float(x)
        if math.isnan(fx):
            return "NA"
        return f"{round(fx*100, 2)}%"
    except Exception:
        return "NA"

lines = []
for i, r in enumerate(top.itertuples(index=False), start=1):
    name = f"Campaign {chr(64+i)}"
    parts = [name + ":"]
    if impr_col and not pd.isna(getattr(r, impr_col)):   parts.append(f"{int(getattr(r, impr_col))} impressions")
    if clicks_col and not pd.isna(getattr(r, clicks_col)): parts.append(f"{int(getattr(r, clicks_col))} clicks")
    if conv_col and not pd.isna(getattr(r, conv_col)):     parts.append(f"{int(getattr(r, conv_col))} conversions")
    # Show CPC/CPA if available; spend often correlates
    if "cpc" in top.columns and not pd.isna(getattr(r, "cpc")): parts.append(f"CPC={fmt_money(getattr(r, 'cpc'))}")
    if "cpa" in top.columns and not pd.isna(getattr(r, "cpa")): parts.append(f"CPA={fmt_money(getattr(r, 'cpa'))}")
    if "ctr" in top.columns and not pd.isna(getattr(r, "ctr")): parts.append(f"CTR={fmt_pct(getattr(r, 'ctr'))}")
    if "cvr" in top.columns and not pd.isna(getattr(r, "cvr")): parts.append(f"CVR={fmt_pct(getattr(r, 'cvr'))}")
    lines.append(" - " + ", ".join(parts))

base_data = "Anonymized Facebook Ads Summary (aggregated):\n" + "\n".join(lines)
instructions = (
    "Use ONLY the statistics shown above. If you reference a metric, "
    "cite the exact numbers you used. Do not assume anything not in the list."
)

prompts = [
    {"id": "neutral", "hypothesis": "H1_framing",
     "prompt": f"{base_data}\n\n{instructions}\n\nTask: Summarize key insights objectively in 5 bullets."},
    {"id": "positive", "hypothesis": "H1_framing",
     "prompt": f"{base_data}\n\n{instructions}\n\nTask: Highlight the most promising campaigns and opportunities for growth in 5 bullets."},
    {"id": "negative", "hypothesis": "H1_framing",
     "prompt": f"{base_data}\n\n{instructions}\n\nTask: Describe the weakest areas and underperforming patterns that need correction in 5 bullets."},
    {"id": "confirmation", "hypothesis": "H2_confirmation",
     "prompt": f"{base_data}\n\n{instructions}\n\nAssume: Higher CTR always implies better performance.\nTask: Write a short rationale supporting this assumption using the data."},
    {"id": "anti_confirmation", "hypothesis": "H2_confirmation",
     "prompt": f"{base_data}\n\n{instructions}\n\nAssume: CTR is misleading; conversions and CPA matter more.\nTask: Write a short rationale supporting this assumption using the data."},
]

with open(os.path.join(OUT_DIR, "prompt_templates.json"), "w") as f:
    json.dump(prompts, f, indent=2)
with open(os.path.join(OUT_DIR, "base_data.txt"), "w") as f:
    f.write(base_data + "\n")

print("✅ Created: prompts/prompt_templates.json and prompts/base_data.txt")
