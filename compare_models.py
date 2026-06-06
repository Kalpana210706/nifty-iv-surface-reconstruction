import pandas as pd

a = pd.read_csv("filled_dataset.csv")
b = pd.read_csv("filled_dataset_cubic.csv")

diff = (a.select_dtypes("number") - b.select_dtypes("number")).abs()

print("Max difference:", diff.max().max())
print("Mean difference:", diff.mean().mean())