import pandas as pd
import matplotlib.pyplot as plt

matches = pd.read_csv("matches.csv")

# Count the number of wins for each team
winner_counts = matches["winner"].value_counts()

print("Distribution of teams that won matches:")
print(winner_counts)

# Create the bar chart
winner_counts.plot(kind="bar")

plt.title("Distribution of Teams That Won Matches")
plt.xlabel("Teams")
plt.ylabel("Number of Wins")
plt.xticks(rotation=90)
plt.tight_layout()

plt.show()