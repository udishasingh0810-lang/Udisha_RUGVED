import pandas as pd

matches = pd.read_csv("matches.csv")

# Remove matches where nobody won by runs
run_wins = matches[matches["win_by_runs"] > 0]

highest = run_wins["win_by_runs"].max()
lowest = run_wins["win_by_runs"].min()

highest_team = run_wins[run_wins["win_by_runs"] == highest]["winner"]
lowest_team = run_wins[run_wins["win_by_runs"] == lowest]["winner"]

print("Team with highest win by runs:")
print(highest_team.to_string(index=False))
print("Runs:", highest)

print("\nTeam with lowest win by runs:")
print(lowest_team.to_string(index=False))
print("Runs:", lowest)