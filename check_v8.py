import pandas as pd

df = pd.read_csv("filled_dataset_surface_v8.csv")

print("Missing:", df.isnull().sum().sum())