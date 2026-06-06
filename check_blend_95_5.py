import pandas as pd

df = pd.read_csv("filled_dataset_blend_95_5.csv")

print("Missing:", df.isnull().sum().sum())