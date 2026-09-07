import pandas as pd

matches = pd.read_csv("matches.csv")

city_counts = matches["city"].value_counts()

print("Total matches conducted city-wise:")
print(city_counts)