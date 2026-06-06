import pandas as pd

df = pd.read_csv("filled_dataset_surface_v6.csv")

option_cols = [
    c for c in df.columns
    if c not in ["datetime", "underlying_price"]
]

for col in option_cols:

    curr = df[col]

    prev1 = curr.shift(1)
    prev2 = curr.shift(2)

    next1 = curr.shift(-1)
    next2 = curr.shift(-2)

    smoothed = (
        0.10 * prev2 +
        0.20 * prev1 +
        0.40 * curr +
        0.20 * next1 +
        0.10 * next2
    )

    # boundaries
    smoothed.iloc[:2] = curr.iloc[:2]
    smoothed.iloc[-2:] = curr.iloc[-2:]

    df[col] = smoothed

df.to_csv(
    "filled_dataset_time_v2.csv",
    index=False
)

print("Saved -> filled_dataset_time_v2.csv")