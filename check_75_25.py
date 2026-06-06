import pandas as pd

df = pd.read_csv("filled_dataset_hybrid_75_25.csv")

print("Missing:", df.isnull().sum().sum())