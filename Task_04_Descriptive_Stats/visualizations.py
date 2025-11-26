import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create output folder
os.makedirs("assets", exist_ok=True)

# Load data
df = pd.read_csv("data/facebook_ads.csv")

# 🔹 Histogram: Estimated Spend
plt.figure(figsize=(8, 5))
sns.histplot(df["estimated_spend"], bins=30, kde=True)
plt.title("Distribution of Estimated Spend")
plt.xlabel("Estimated Spend")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("assets/spend_hist.png")
plt.close()

# 🔹 Bar chart: Top 10 Bylines
top_bylines = df["bylines"].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_bylines.values, y=top_bylines.index)
plt.title("Top 10 Mentioned Bylines")
plt.xlabel("Frequency")
plt.ylabel("Bylines")
plt.tight_layout()
plt.savefig("assets/byline_bar.png")
plt.close()

# 🔹 Boxplot: Estimated Impressions
plt.figure(figsize=(8, 5))
sns.boxplot(x=df["estimated_impressions"])
plt.title("Boxplot of Estimated Impressions")
plt.xlabel("Estimated Impressions")
plt.tight_layout()
plt.savefig("assets/impressions_box.png")
plt.close()
