import pandas as pd

strike = pd.read_csv("filled_dataset_time_strike_v2.csv")
xgb = pd.read_csv("filled_dataset_xgb.csv")

option_cols = [
    c for c in strike.columns
    if c not in ["datetime", "underlying_price"]
]

out = strike.copy()

out[option_cols] = (
    0.90 * strike[option_cols]
    + 0.10 * xgb[option_cols]
)

out.to_csv(
    "filled_dataset_strike_xgb_90_10.csv",
    index=False
)

print("Saved -> filled_dataset_strike_xgb_90_10.csv")