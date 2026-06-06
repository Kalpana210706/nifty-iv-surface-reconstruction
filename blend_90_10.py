import pandas as pd

a = pd.read_csv("filled_dataset_time_v1.csv")
b = pd.read_csv("filled_dataset_surface_v6.csv")

option_cols = [
    c for c in a.columns
    if c not in ["datetime", "underlying_price"]
]

out = a.copy()

out[option_cols] = (
    0.90 * a[option_cols] +
    0.10 * b[option_cols]
)

out.to_csv(
    "filled_dataset_blend_90_10.csv",
    index=False
)

print("Saved -> filled_dataset_blend_90_10.csv")