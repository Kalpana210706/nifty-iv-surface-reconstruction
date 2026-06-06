import pandas as pd

a = pd.read_csv("filled_dataset_surface_v6.csv")
b = pd.read_csv("filled_dataset_time_v1.csv")

cols = [
    c for c in a.columns
    if c not in ["datetime","underlying_price"]
]

diff = (a[cols]-b[cols]).abs()

print("Mean diff:", diff.mean().mean())
print("Max diff:", diff.max().max())