import pandas as pd
import numpy as np

df = pd.read_csv("dataset.csv")

# df["datetime"] = pd.to_datetime(df["datetime"])
# df["datetime"] = pd.to_datetime(
#     df["datetime"],
#     dayfirst=True
# )
df["datetime"] = pd.to_datetime(
    df["datetime"],
    format="%d-%m-%Y %H:%M"
)

option_cols = [
    c for c in df.columns
    if c not in ["datetime", "underlying_price"]
]

rows = []

for col in option_cols:

    strike = int(col[-7:-2])

    option_type = 1 if col.endswith("CE") else 0

    temp = pd.DataFrame({
        "datetime": df["datetime"],
        "underlying_price": df["underlying_price"],
        "hour": df["datetime"].dt.hour,
        "minute": df["datetime"].dt.minute,
        "strike": strike,
        "option_type": option_type,
        "iv": df[col]
    })

    temp["option_name"] = col

    rows.append(temp)

long_df = pd.concat(rows, ignore_index=True)

print(long_df.head())

print()
print("Shape:", long_df.shape)

long_df.to_csv("long_dataset.csv", index=False)