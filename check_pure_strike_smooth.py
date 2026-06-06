import pandas as pd

df = pd.read_csv("filled_dataset_pure_strike_smooth.csv")

print("Missing:", df.isnull().sum().sum())
print("Shape:", df.shape)