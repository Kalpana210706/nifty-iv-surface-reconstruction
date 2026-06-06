import pandas as pd

df = pd.read_csv(
    "filled_dataset_hybrid_xgb_99_1.csv"
)

print(df.isnull().sum().sum())
