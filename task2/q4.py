import pandas as pd

matches = pd.read_csv("matches.csv")

toss_decisions = matches.groupby(
    ["toss_winner", "toss_decision"]
).size()

print("Toss decisions taken by each team:")
print(toss_decisions)