import pandas as pd

df = pd.read_csv("dataset.csv")

filled_df = df.copy()

option_cols = [
    c for c in df.columns
    if c not in ["datetime", "underlying_price"]
]

print("Pass 1: Strike-wise interpolation")

# STRIKE DIRECTION
for idx in filled_df.index:

    row = filled_df.loc[idx, option_cols]

    try:
        row = (
            row
            .interpolate(method="cubic")
            .bfill()
            .ffill()
        )

    except:
        row = (
            row
            .interpolate(method="linear")
            .bfill()
            .ffill()
        )

    filled_df.loc[idx, option_cols] = row

print("Pass 2: Time-wise interpolation")

# TIME DIRECTION
for col in option_cols:

    try:
        filled_df[col] = (
            filled_df[col]
            .interpolate(method="cubic")
            .bfill()
            .ffill()
        )

    except:
        filled_df[col] = (
            filled_df[col]
            .interpolate(method="linear")
            .bfill()
            .ffill()
        )

filled_df.to_csv(
    "filled_dataset_surface_v3.csv",
    index=False
)

print("Saved -> filled_dataset_surface_v3.csv")