import pandas as pd

df = pd.read_csv("filled_dataset_strike_xgb_90_10.csv")

print("Missing:", df.isnull().sum().sum())