import pandas as pd

df = pd.read_csv("dataset.csv")

option_cols = [
    c for c in df.columns
    if c not in ["datetime", "underlying_price"]
]

print("Total option columns:", len(option_cols))

for col in option_cols:
    print(col)