import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error

df = pd.read_csv("dataset.csv")

numeric_cols = [c for c in df.columns if c != "datetime"]

temp = df.copy()

# known values ka 10% randomly hide karenge
np.random.seed(42)

masked_positions = []

for col in numeric_cols:

    valid_idx = temp[temp[col].notna()].index

    sample_size = max(1, int(0.1 * len(valid_idx)))

    chosen = np.random.choice(
        valid_idx,
        size=sample_size,
        replace=False
    )

    for idx in chosen:
        masked_positions.append(
            (idx, col, temp.loc[idx, col])
        )
        temp.loc[idx, col] = np.nan

# interpolation
for col in numeric_cols:
    temp[col] = (
        temp[col]
        .interpolate()
        .bfill()
        .ffill()
    )

# MSE calculate
actual = []
predicted = []

for idx, col, value in masked_positions:

    actual.append(value)
    predicted.append(temp.loc[idx, col])

mse = mean_squared_error(
    actual,
    predicted
)

print("Validation MSE =", mse)