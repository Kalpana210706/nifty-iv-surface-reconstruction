import pandas as pd
import numpy as np

df = pd.read_csv("long_dataset.csv")

# Sort properly
df = df.sort_values(
    ["option_name", "datetime"]
).reset_index(drop=True)

# Previous time IV
df["prev_iv"] = (
    df.groupby("option_name")["iv"]
      .shift(1)
)

# Next time IV
df["next_iv"] = (
    df.groupby("option_name")["iv"]
      .shift(-1)
)

print(df.head())

print()
print("Missing IVs:", df["iv"].isna().sum())

df.to_csv(
    "long_dataset_features.csv",
    index=False
)

print("Saved.")