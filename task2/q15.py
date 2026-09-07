import pandas as pd

matches = pd.read_csv("matches.csv")
deliveries = pd.read_csv("deliveries.csv")

# Calculate total runs for each match
match_runs = deliveries.groupby("match_id")["total_runs"].sum().reset_index()

# Add season information
match_runs = match_runs.merge(
    matches[["id", "season"]],
    left_on="match_id",
    right_on="id"
)

# Calculate total runs for each season
season_runs = match_runs.groupby("season")["total_runs"].sum()

print("Total runs scored in each season:")
print(season_runs)