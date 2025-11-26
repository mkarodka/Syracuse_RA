import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("WBBStatsFile01.csv")

# Strip any leading/trailing spaces in column names
df.columns = df.columns.str.strip()

# Confirm columns
print("Columns:", df.columns.tolist())

# 1. Bar chart of Wins vs. Teams
top_wins = df.sort_values(by="Wins", ascending=False).head(10)
plt.figure(figsize=(10,6))
sns.barplot(x="Wins", y="Team", data=top_wins, palette="viridis", dodge=False)
plt.title("Top 10 Teams by Wins")
plt.tight_layout()
plt.savefig("wins_vs_teams.png")
plt.show()

# 2. Scatter plot: TotalAssist vs. Total Turnovers
plt.figure(figsize=(10,6))
sns.scatterplot(x="TotalAssist", y="Total Turnovers", data=df, hue="Team", legend=False)
plt.title("Total Assists vs. Total Turnovers")
plt.xlabel("Total Assists")
plt.ylabel("Total Turnovers")
plt.tight_layout()
plt.savefig("assists_vs_turnovers.png")
plt.show()

# 3. Bar chart: Opponent FG% vs Teams
top_defense = df.sort_values(by="Opponent FG %").head(10)
plt.figure(figsize=(10,6))
sns.barplot(x="Opponent FG %", y="Team", data=top_defense, palette="mako", dodge=False)
plt.title("Top 10 Teams by Lowest Opponent FG%")
plt.tight_layout()
plt.savefig("opponent_fg_pct_vs_teams.png")
plt.show()

# 4. Blocks Per Game vs Teams
top_blocks = df.sort_values(by="BlocksPerGame", ascending=False).head(10)
plt.figure(figsize=(10,6))
sns.barplot(x="BlocksPerGame", y="Team", data=top_blocks, palette="rocket", dodge=False)
plt.title("Top 10 Teams by Blocks Per Game")
plt.tight_layout()
plt.savefig("blocks_per_game_vs_teams.png")
plt.show()

# 5. Free Throw Percentage vs Teams
top_ft_pct = df.sort_values(by="Free Throw Percentage Season", ascending=False).head(10)
plt.figure(figsize=(10,6))
sns.barplot(x="Free Throw Percentage Season", y="Team", data=top_ft_pct, palette="coolwarm", dodge=False)
plt.title("Top 10 Teams by Free Throw Percentage")
plt.tight_layout()
plt.savefig("free_throw_pct_vs_teams.png")
plt.show()
