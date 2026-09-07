import pandas as pd

matches = pd.read_csv("matches.csv")

mean_runs = matches["win_by_runs"].mean()
median_runs = matches["win_by_runs"].median()
std_runs = matches["win_by_runs"].std()

print("Mean:", mean_runs)
print("Median:", median_runs)
print("Standard Deviation:", std_runs)