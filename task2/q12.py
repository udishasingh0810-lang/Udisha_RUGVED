import pandas as pd

matches = pd.read_csv("matches.csv")
deliveries = pd.read_csv("deliveries.csv")

# Calculate total runs for each match
match_runs = deliveries.groupby("match_id")["total_runs"].sum().reset_index()

# Add venue information
match_runs = match_runs.merge(
    matches[["id", "venue"]],
    left_on="match_id",
    right_on="id"
)

# Calculate average runs at each venue
average_runs = match_runs.groupby("venue")["total_runs"].mean()

print("Average runs scored at each venue:")
print(average_runs)