import pandas as pd

matches = pd.read_csv("matches.csv")

total_matches = len(matches[matches["season"] == 2008])

print("Total matches conducted in 2008:", total_matches)