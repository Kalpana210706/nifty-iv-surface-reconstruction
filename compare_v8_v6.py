import pandas as pd

v6 = pd.read_csv("filled_dataset_surface_v6.csv")
v8 = pd.read_csv("filled_dataset_surface_v8.csv")

cols = [c for c in v6.columns if c not in ["datetime","underlying_price"]]

diff = (v6[cols] - v8[cols]).abs()

print("Mean diff:", diff.mean().mean())
print("Max diff:", diff.max().max())