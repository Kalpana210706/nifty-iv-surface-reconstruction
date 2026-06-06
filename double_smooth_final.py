import pandas as pd

df = pd.read_csv("filled_dataset_time_strike_v2.csv")

option_cols = [
    c for c in df.columns
    if c not in ["datetime", "underlying_price"]
]

# Pass 1
for col in option_cols:

    prev = df[col].shift(1)
    curr = df[col]
    nxt = df[col].shift(-1)

    smoothed = (
        0.15 * prev +
        0.70 * curr +
        0.15 * nxt
    )

    smoothed.iloc[0] = curr.iloc[0]
    smoothed.iloc[-1] = curr.iloc[-1]

    df[col] = smoothed

# Pass 2
for col in option_cols:

    prev = df[col].shift(1)
    curr = df[col]
    nxt = df[col].shift(-1)

    smoothed = (
        0.15 * prev +
        0.70 * curr +
        0.15 * nxt
    )

    smoothed.iloc[0] = curr.iloc[0]
    smoothed.iloc[-1] = curr.iloc[-1]

    df[col] = smoothed

df.to_csv(
    "filled_dataset_double_smooth_final.csv",
    index=False
)

print("Saved -> filled_dataset_double_smooth_final.csv")