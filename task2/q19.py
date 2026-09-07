import pandas as pd
import matplotlib.pyplot as plt

matches = pd.read_csv("matches.csv")

# Count toss decisions for each season
toss_data = pd.crosstab(
    matches["season"],
    matches["toss_decision"]
)

# Create the bar chart
toss_data.plot(kind="bar")

plt.title("Toss Decisions Across Seasons")
plt.xlabel("Season")
plt.ylabel("Number of Toss Decisions")
plt.xticks(rotation=45)
plt.legend(title="Toss Decision")
plt.tight_layout()

plt.show()