import pandas as pd

time = pd.read_csv("filled_dataset_time_v1.csv")
xgb = pd.read_csv("filled_dataset_xgb.csv")

option_cols = [
    c for c in time.columns
    if c not in ["datetime", "underlying_price"]
]

out = time.copy()

out[option_cols] = (
    0.99 * time[option_cols]
    + 0.01 * xgb[option_cols]
)

out.to_csv(
    "filled_dataset_hybrid_xgb_99_1.csv",
    index=False
)

print("Saved")