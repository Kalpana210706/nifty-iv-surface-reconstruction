import pandas as pd
from sklearn.impute import KNNImputer

df = pd.read_csv("dataset.csv")

datetime_col = df["datetime"]

numeric_df = df.drop(columns=["datetime"])

imputer = KNNImputer(
    n_neighbors=5,
    weights="distance"
)

filled = imputer.fit_transform(numeric_df)

filled_df = pd.DataFrame(
    filled,
    columns=numeric_df.columns
)

filled_df.insert(0, "datetime", datetime_col)

filled_df.to_csv(
    "filled_dataset_knn.csv",
    index=False
)

print("Done")