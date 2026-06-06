import pandas as pd

df = pd.read_csv("filled_dataset_time_v2.csv")

print("Missing:", df.isnull().sum().sum())