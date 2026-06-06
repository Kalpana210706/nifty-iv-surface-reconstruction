import pandas as pd
import numpy as np

v6 = pd.read_csv("filled_dataset_surface_v6.csv")
xgb = pd.read_csv("filled_dataset_xgb.csv")

option_cols = [
    c for c in v6.columns
    if c not in ["datetime", "underlying_price"]
]

diff = np.abs(
    v6[option_cols] - xgb[option_cols]
)

print("Mean Difference:", diff.mean().mean())
print("Max Difference:", diff.max().max())