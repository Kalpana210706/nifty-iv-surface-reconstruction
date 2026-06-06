import pandas as pd

df = pd.read_csv("filled_dataset_time_v1.csv")

option_cols = [
    c for c in df.columns
    if c not in ["datetime", "underlying_price"]
]

for i in range(len(df)):

    row = df.loc[i, option_cols].copy()

    smoothed = row.copy()

    for j in range(1, len(option_cols) - 1):

        smoothed.iloc[j] = (
            0.25 * row.iloc[j - 1] +
            0.50 * row.iloc[j] +
            0.25 * row.iloc[j + 1]
        )

    df.loc[i, option_cols] = smoothed

df.to_csv(
    "filled_dataset_time_strike_v1.csv",
    index=False
)

print("Saved -> filled_dataset_time_strike_v1.csv")