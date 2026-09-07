import pandas as pd

matches = pd.read_csv("matches.csv")

result_counts = matches["result"].value_counts()

print("Match results:")
print(result_counts)
