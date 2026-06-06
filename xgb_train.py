import pandas as pd
import numpy as np
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error

# df = pd.read_csv("long_dataset_features.csv")
df = pd.read_csv("long_dataset_neighbors.csv")

df["left_strike_iv"] = df["left_strike_iv"].fillna(df["iv"])
df["right_strike_iv"] = df["right_strike_iv"].fillna(df["iv"])

# Training rows
train_df = df[df["iv"].notna()].copy()

# Missing rows
test_df = df[df["iv"].isna()].copy()

# features = [
#     "underlying_price",
#     "hour",
#     "minute",
#     "strike",
#     "option_type",
#     "prev_iv",
#     "next_iv"
# ]

features = [
    "underlying_price",
    "hour",
    "minute",
    "strike",
    "option_type",
    "prev_iv",
    "next_iv",
    "left_strike_iv",
    "right_strike_iv"
]

# Fill feature NaNs
train_df[features] = train_df[features].fillna(
    train_df[features].median()
)

test_df[features] = test_df[features].fillna(
    train_df[features].median()
)

X_train = train_df[features]
y_train = train_df["iv"]

print("Training XGB...")

model = XGBRegressor(
    n_estimators=300,
    max_depth=6,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42
)

model.fit(X_train, y_train)

print("Training Complete")

preds = model.predict(test_df[features])

df.loc[df["iv"].isna(), "iv"] = preds

df.to_csv(
    "xgb_predictions.csv",
    index=False
)

print("Saved xgb_predictions.csv")