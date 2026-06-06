# # import pandas as pd

# # df = pd.read_csv("dataset.csv")

# # print(df.iloc[:3,:5])

# import pandas as pd

# df = pd.read_csv("dataset.csv")

# print(df.shape)

# print(df.head())

import pandas as pd

df = pd.read_csv("dataset.csv")

df["datetime"] = pd.to_datetime(
    df["datetime"],
    format="%d-%m-%Y %H:%M"
)

print(df.head())

df["hour"] = df["datetime"].dt.hour

df["minute"] = df["datetime"].dt.minute

print(
    df[["hour","minute"]].head()
)

long_df = []

for col in df.columns:

    if (
        col not in
        [
            "datetime",
            "underlying_price",
            "hour",
            "minute"
        ]
    ):

        temp = pd.DataFrame()

        temp["datetime"] = df["datetime"]

        temp["underlying_price"] = df["underlying_price"]

        temp["hour"] = df["hour"]

        temp["minute"] = df["minute"]

        temp["option"] = col

        temp["iv"] = df[col]

        long_df.append(temp)

long_df = pd.concat(
    long_df,
    ignore_index=True
)

print(long_df.head())

print(long_df.shape)
import re

def get_strike(name):

    match = re.search(r'(\d{5})(CE|PE)$', name)

    if match:
        return int(match.group(1))

    return None

long_df["strike"] = (
    long_df["option"]
    .apply(get_strike)
)

print(
    long_df[
        ["option","strike"]
    ].head()
)

long_df["option_type"] = (
    long_df["option"]
    .str[-2:]
)

print(
    long_df[
        ["option_type"]
    ].head()
)

long_df["moneyness"] = (
    long_df["strike"]
    - long_df["underlying_price"]
)

print(
    long_df[
        [
            "strike",
            "underlying_price",
            "moneyness"
        ]
    ].head()
)

long_df["option_type"] = (
    long_df["option_type"]
    .map({
        "CE": 0,
        "PE": 1
    })
)

train_df = long_df[
    long_df["iv"].notna()
]

test_df = long_df[
    long_df["iv"].isna()
]

print("Train Shape:", train_df.shape)
print("Test Shape:", test_df.shape)


from sklearn.ensemble import RandomForestRegressor

features = [
    "underlying_price",
    "hour",
    "minute",
    "strike",
    "moneyness",
    "option_type"
]

X_train = train_df[features]
y_train = train_df["iv"]

X_test = test_df[features]

print("Training RF...")

rf = RandomForestRegressor(
    n_estimators=200,
    max_depth=12,
    random_state=42,
    n_jobs=-1
)

rf.fit(X_train, y_train)

print("Training Complete")

predictions = rf.predict(X_test)

print(predictions[:10])


filled_long = long_df.copy()

filled_long.loc[
    filled_long["iv"].isna(),
    "iv"
] = predictions

print(
    filled_long["iv"].isna().sum()
)

# Put predictions back
filled_long = long_df.copy()

filled_long.loc[
    filled_long["iv"].isna(),
    "iv"
] = predictions

# Rebuild original wide dataset
filled_df = df.copy()

for option_name in filled_long["option"].unique():

    option_data = filled_long[
        filled_long["option"] == option_name
    ]["iv"].values

    filled_df[option_name] = option_data

filled_df.to_csv(
    "filled_dataset_rf.csv",
    index=False
)

print("Saved -> filled_dataset_rf.csv")