import pandas as pd
import numpy as np

df = pd.read_csv("long_dataset_features.csv")

# option order
options = sorted(df["option_name"].unique())

left_map = {}
right_map = {}

for i, op in enumerate(options):

    if i > 0:
        left_map[op] = options[i-1]
    else:
        left_map[op] = None

    if i < len(options)-1:
        right_map[op] = options[i+1]
    else:
        right_map[op] = None

df["left_strike_iv"] = np.nan
df["right_strike_iv"] = np.nan

lookup = {}

for _, row in df.iterrows():
    lookup[(row["datetime"], row["option_name"])] = row["iv"]

for idx, row in df.iterrows():

    dt = row["datetime"]

    left_op = left_map[row["option_name"]]
    right_op = right_map[row["option_name"]]

    if left_op:
        df.at[idx, "left_strike_iv"] = lookup.get(
            (dt, left_op),
            np.nan
        )

    if right_op:
        df.at[idx, "right_strike_iv"] = lookup.get(
            (dt, right_op),
            np.nan
        )

df.to_csv(
    "long_dataset_neighbors.csv",
    index=False
)

print(df.head())
print("Saved.")