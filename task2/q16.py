import pandas as pd

deliveries = pd.read_csv("deliveries.csv")

# Calculate total runs scored by each batsman
batsman_runs = deliveries.groupby("batsman")["batsman_runs"].sum()

# Sort from highest to lowest and get top 10
top_10 = batsman_runs.sort_values(ascending=False).head(10)

print("Top 10 batsmen by total runs:")
print(top_10)