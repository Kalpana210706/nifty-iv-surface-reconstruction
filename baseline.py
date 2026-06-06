import pandas as pd

df = pd.read_csv("dataset.csv")

filled_df = df.copy()

for col in filled_df.columns:

    if col not in ["datetime"]:

        filled_df[col] = (
            filled_df[col]
            .interpolate(method="linear")
            .bfill()
            .ffill()
        )

filled_df.to_csv("filled_dataset.csv", index=False)

print("Done")