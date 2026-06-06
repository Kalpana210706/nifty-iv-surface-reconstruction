import pandas as pd
import numpy as np

df = pd.read_csv("dataset.csv")

option_cols = [
    c for c in df.columns
    if c not in ["datetime", "underlying_price"]
]

# ROW MODEL
row_df = df.copy()

for idx in row_df.index:

    row = row_df.loc[idx, option_cols]

    row = (
        row
        .interpolate(method="linear")
        .bfill()
        .ffill()
    )

    row_df.loc[idx, option_cols] = row

# COLUMN MODEL
col_df = df.copy()

for col in option_cols:

    col_df[col] = (
        col_df[col]
        .interpolate(method="cubic")
        .bfill()
        .ffill()
    )

# ENSEMBLE
final_df = df.copy()

for col in option_cols:

    final_df[col] = (
        row_df[col] +
        col_df[col]
    ) / 2

final_df.to_csv(
    "filled_dataset_surface_v4.csv",
    index=False
)

print("Saved -> filled_dataset_surface_v4.csv")

print(
    "Missing:",
    final_df.isnull().sum().sum()
)