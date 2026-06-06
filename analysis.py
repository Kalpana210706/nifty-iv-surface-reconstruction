# import pandas as pd

# df = pd.read_csv("dataset.csv")

# print("Shape:", df.shape)
# print("\nColumns:")
# print(df.columns)

# print("\nMissing Values:")
# print(df.isnull().sum())

# print("\nTotal Missing Values:")
# print(df.isnull().sum().sum())

import pandas as pd

df = pd.read_csv("dataset.csv")

print(df.columns.tolist())
print()
print(df.shape)
print()
print(df.isnull().sum())
print(df.head())

print(df.columns.tolist())