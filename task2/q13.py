import pandas as pd

matches = pd.read_csv("matches.csv")

# Combine all umpire columns
umpires = pd.concat([
    matches["umpire1"],
    matches["umpire2"],
    matches["umpire3"]
])

# Count how many times each umpire appeared
umpire_counts = umpires.dropna().value_counts()

# Find the maximum count
maximum = umpire_counts.max()

print("Umpire(s) who umpired the maximum number of times:")
print(umpire_counts[umpire_counts == maximum])

print("\nMaximum number of matches:", maximum)