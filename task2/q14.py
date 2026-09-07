import pandas as pd

matches = pd.read_csv("matches.csv")

season_counts = matches["season"].value_counts().sort_index()

print("Total matches in each season:")
print(season_counts)