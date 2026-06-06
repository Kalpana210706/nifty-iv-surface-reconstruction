import pandas as pd

df = pd.read_csv("filled_dataset_time_strike_v3.csv")

print("Missing:", df.isnull().sum().sum())