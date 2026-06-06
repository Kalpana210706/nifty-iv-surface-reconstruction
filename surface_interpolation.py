# import pandas as pd

# df = pd.read_csv("dataset.csv")

# filled_df = df.copy()

# # datetime ko touch nahi karenge
# option_cols = [c for c in df.columns if c not in ["datetime", "underlying_price"]]

# for col in option_cols:
#     filled_df[col] = (
#         filled_df[col]
#         .interpolate(method="cubic")
#         .bfill()
#         .ffill()
#     )

# filled_df.to_csv("filled_dataset_cubic.csv", index=False)

# print("Saved -> filled_dataset_cubic.csv")

import pandas as pd

df = pd.read_csv("dataset.csv")

filled_df = df.copy()

option_cols = [
    c for c in df.columns
    if c not in ["datetime", "underlying_price"]
]

# PASS 1: Strike-wise interpolation
for idx in filled_df.index:

    row = filled_df.loc[idx, option_cols]

    row = (
        row
        .interpolate(method="linear")
        .bfill()
        .ffill()
    )

    filled_df.loc[idx, option_cols] = row

# PASS 2: Time-wise interpolation
for col in option_cols:

    filled_df[col] = (
        filled_df[col]
        .interpolate(method="cubic")
        .bfill()
        .ffill()
    )

filled_df.to_csv(
    "filled_dataset_surface_v2.csv",
    index=False
)

print("Saved -> filled_dataset_surface_v2.csv")