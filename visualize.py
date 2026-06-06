import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")

plt.figure(figsize=(15,8))
sns.heatmap(df.isnull())
plt.show()