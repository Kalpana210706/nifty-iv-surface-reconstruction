import pandas as pd

v1 = pd.read_csv("filled_dataset_time_v1.csv")
ts = pd.read_csv("filled_dataset_time_strike_v1.csv")

option_cols = [
    c for c in v1.columns
    if c not in ["datetime", "underlying_price"]
]

diff = (v1[option_cols] - ts[option_cols]).abs()

print("Mean diff:", diff.mean().mean())
print("Max diff:", diff.max().max())