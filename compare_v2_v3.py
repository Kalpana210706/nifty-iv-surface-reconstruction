import pandas as pd

v2 = pd.read_csv("filled_dataset_surface_v2.csv")
v3 = pd.read_csv("filled_dataset_surface_v3.csv")

diff = 0

for col in v2.columns:
    if col not in ["datetime", "underlying_price"]:
        diff += (v2[col] - v3[col]).abs().sum()

print("Total difference:", diff)