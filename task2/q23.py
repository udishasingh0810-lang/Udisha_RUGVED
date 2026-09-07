import pandas as pd
import matplotlib.pyplot as plt

matches = pd.read_csv("matches.csv")

# Count the number of wins for each team
top_5 = matches["winner"].value_counts().head(5)

print("Top 5 teams with most wins:")
print(top_5)

# Create the bar chart
top_5.plot(kind="bar")

plt.title("Top 5 Teams with Most Wins Across All Seasons")
plt.xlabel("Teams")
plt.ylabel("Number of Wins")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()