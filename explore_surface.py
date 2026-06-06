import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset.csv")

# first timestamp
row = df.iloc[0]

cols = [c for c in df.columns if "CE" in c]

strikes = []

ivs = []

for col in cols:

    strike = int(col[-7:-2])

    val = row[col]

    if pd.notna(val):

        strikes.append(strike)

        ivs.append(val)

plt.plot(strikes, ivs, marker="o")

plt.title("IV Smile")

plt.show()