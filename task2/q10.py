import pandas as pd

matches = pd.read_csv("matches.csv")

player_counts = matches["player_of_match"].value_counts()

players = player_counts[player_counts > 3]

print("Players who won Player of the Match more than 3 times:")
print(players)