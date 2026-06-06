import pandas as pd

df = pd.read_csv("filled_dataset_rf.csv")

print(
    "Missing values:",
    df.isnull().sum().sum()
)
