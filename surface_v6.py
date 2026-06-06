import pandas as pd

df = pd.read_csv("filled_dataset_surface_v4.csv")

option_cols = [
    c for c in df.columns
    if c not in ["datetime", "underlying_price"]
]

smooth_df = df.copy()

for i in range(1, len(option_cols)-1):

    left_col = option_cols[i-1]
    curr_col = option_cols[i]
    right_col = option_cols[i+1]

    smooth_df[curr_col] = (
        0.25 * df[left_col]
        +
        0.50 * df[curr_col]
        +
        0.25 * df[right_col]
    )

smooth_df.to_csv(
    "filled_dataset_surface_v6.csv",
    index=False
)

print(
    "Missing:",
    smooth_df.isnull().sum().sum()
)

print("Saved V6")