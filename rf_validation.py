import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

df = pd.read_csv("dataset.csv")

# option columns
option_cols = [
    c for c in df.columns
    if c not in ["datetime", "underlying_price"]
]

# choose one column for validation
target_col = option_cols[0]

temp = df.copy()

# known values
known_idx = temp[temp[target_col].notna()].index

np.random.seed(42)

hide_idx = np.random.choice(
    known_idx,
    size=int(0.2 * len(known_idx)),
    replace=False
)

actual_values = temp.loc[
    hide_idx,
    target_col
].copy()

temp.loc[
    hide_idx,
    target_col
] = np.nan

# simple interpolation
filled = (
    temp[target_col]
    .interpolate()
    .bfill()
    .ffill()
)

mse = mean_squared_error(
    actual_values,
    filled.loc[hide_idx]
)

print("Interpolation MSE:", mse)