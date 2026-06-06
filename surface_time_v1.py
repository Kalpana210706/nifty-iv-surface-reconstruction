import pandas as pd

df = pd.read_csv("filled_dataset_surface_v6.csv")

option_cols = [
    c for c in df.columns
    if c not in ["datetime", "underlying_price"]
]

for col in option_cols:

    prev = df[col].shift(1)
    curr = df[col]
    nxt = df[col].shift(-1)

    smoothed = (
        0.25 * prev +
        0.50 * curr +
        0.25 * nxt
    )

    smoothed.iloc[0] = curr.iloc[0]
    smoothed.iloc[-1] = curr.iloc[-1]

    df[col] = smoothed

df.to_csv(
    "filled_dataset_time_v1.csv",
    index=False
)

print("Saved")