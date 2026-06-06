import pandas as pd

orig = pd.read_csv("dataset.csv")
pred = pd.read_csv("xgb_predictions.csv")

option_cols = [
    c for c in orig.columns
    if c not in ["datetime", "underlying_price"]
]

filled = orig.copy()

for col in option_cols:

    temp = pred[pred["option_name"] == col]

    filled[col] = temp["iv"].values

filled.to_csv(
    "filled_dataset_xgb.csv",
    index=False
)

print("Saved filled_dataset_xgb.csv")
print("Missing:", filled.isnull().sum().sum())