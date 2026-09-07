import pandas as pd

matches = pd.read_csv("matches.csv")

tied_matches = matches[matches["result"] == "tie"]

print("Teams involved in tied matches:")
print(tied_matches[["team1", "team2"]])