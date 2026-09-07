import pandas as pd

deliveries = pd.read_csv("deliveries.csv")

# Remove deliveries where no player was dismissed
dismissals = deliveries[deliveries["player_dismissed"].notna()]

# Count wickets taken by each bowler
wickets = dismissals.groupby("bowler").size()

# Sort from highest to lowest
wickets = wickets.sort_values(ascending=False)

print("Total wickets taken by each bowler:")
print(wickets)