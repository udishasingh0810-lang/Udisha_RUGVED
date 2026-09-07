import pandas as pd

deliveries = pd.read_csv("deliveries.csv")

sixes = deliveries[deliveries["batsman_runs"] == 6]

print("Deliveries where the batsman scored a six:")
print(sixes[["match_id", "inning", "over", "ball", "batsman", "bowler", "batsman_runs"]])