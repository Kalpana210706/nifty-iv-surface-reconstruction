import pandas as pd

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

# 20% row + 80% column
final_df = df.copy()

for col in option_cols:

    final_df[col] = (
        0.2 * row_df[col]
        +
        0.8 * col_df[col]
    )

final_df.to_csv(
    "filled_dataset_surface_v5_80.csv",
    index=False
)

print(
    "Missing:",
    final_df.isnull().sum().sum()
)