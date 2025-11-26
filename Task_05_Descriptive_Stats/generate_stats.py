import pandas as pd

# Load the dataset
df = pd.read_csv("WBBStatsFile01.csv")

# Basic info
print("Columns:", df.columns.tolist())
print("\nFirst 5 rows:")
print(df.head())

# Summary statistics for numeric columns
print("\nSummary Statistics:")
print(df.describe())

# Check for missing values
print("\nMissing values count:")
print(df.isnull().sum())

# Top 5 teams by Wins
print("\nTop 5 Teams by Wins:")
top_wins = df.sort_values(by="Wins", ascending=False).head(5)
print(top_wins[["Team", "Wins", "Losses", "Games"]])

# Top 5 teams by Assist-Turnover Ratio
print("\nTop 5 Teams by Assist-Turnover Ratio:")
top_at_ratio = df.sort_values(by="AssistTurnoverRatio", ascending=False).head(5)
print(top_at_ratio[["Team", "AssistTurnoverRatio"]])

# Top 5 teams by Defense (lowest Opponent FG %)
print("\nTop 5 Teams by Defense (Lowest Opponent FG %):")
top_defense = df.sort_values(by="Opponent FG %").head(5)
print(top_defense[["Team", "Opponent FG %"]])

# Save top 10 teams by wins into subset.csv for LLM input
subset = df.sort_values(by="Wins", ascending=False).head(10)
subset.to_csv("subset.csv", index=False)
print("\nSaved top 10 teams by Wins into 'subset.csv'")
