import pandas as pd

deliveries = pd.read_csv("deliveries.csv")

# Total runs scored by each batsman
total_runs = deliveries.groupby("batsman")["batsman_runs"].sum()

# Number of times each batsman was dismissed
dismissals = deliveries[deliveries["player_dismissed"].notna()]
dismissal_counts = dismissals.groupby("player_dismissed").size()

# Calculate batting average
batting_average = total_runs / dismissal_counts

# Remove players who have never been dismissed
batting_average = batting_average.dropna()

# Sort and get top 10
top_10 = batting_average.sort_values(ascending=False).head(10)

print("Top 10 batsmen by batting average:")
print(top_10)