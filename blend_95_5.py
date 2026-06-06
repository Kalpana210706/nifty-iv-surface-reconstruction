import pandas as pd

time_v1 = pd.read_csv("filled_dataset_time_v1.csv")
surface_v6 = pd.read_csv("filled_dataset_surface_v6.csv")

option_cols = [
    c for c in time_v1.columns
    if c not in ["datetime", "underlying_price"]
]

out = time_v1.copy()

out[option_cols] = (
    0.95 * time_v1[option_cols]
    + 0.05 * surface_v6[option_cols]
)

out.to_csv(
    "filled_dataset_blend_95_5.csv",
    index=False
)

print("Saved -> filled_dataset_blend_95_5.csv")