# hybrid_time_strike_70_30.py

import pandas as pd

time = pd.read_csv("filled_dataset_time_v1.csv")
strike = pd.read_csv("filled_dataset_time_strike_v2.csv")

option_cols = [
    c for c in time.columns
    if c not in ["datetime", "underlying_price"]
]

out = time.copy()

out[option_cols] = (
    0.70 * time[option_cols]
    + 0.30 * strike[option_cols]
)

out.to_csv(
    "filled_dataset_hybrid_70_30.csv",
    index=False
)

print("Saved")