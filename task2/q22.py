import pandas as pd
import matplotlib.pyplot as plt

matches = pd.read_csv("matches.csv")

# Count toss decisions made by each team
toss_outcomes = pd.crosstab(
    matches["toss_winner"],
    matches["toss_decision"]
)

print("Toss outcomes of all teams:")
print(toss_outcomes)

# Create the bar chart
toss_outcomes.plot(kind="bar")

plt.title("Toss Outcomes of All Teams")
plt.xlabel("Teams")
plt.ylabel("Number of Toss Decisions")
plt.xticks(rotation=90)
plt.legend(title="Toss Decision")
plt.tight_layout()

plt.show()