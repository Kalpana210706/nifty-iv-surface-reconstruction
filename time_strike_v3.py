import pandas as pd

df = pd.read_csv("filled_dataset_time_v1.csv")

ce_cols = [c for c in df.columns if c.endswith("CE")]
pe_cols = [c for c in df.columns if c.endswith("PE")]

for i in range(len(df)):

    # CE smoothing
    row = df.loc[i, ce_cols].copy()
    smooth = row.copy()

    for j in range(1, len(ce_cols) - 1):
        smooth.iloc[j] = (
            0.30 * row.iloc[j - 1] +
            0.40 * row.iloc[j] +
            0.30 * row.iloc[j + 1]
        )

    df.loc[i, ce_cols] = smooth

    # PE smoothing
    row = df.loc[i, pe_cols].copy()
    smooth = row.copy()

    for j in range(1, len(pe_cols) - 1):
        smooth.iloc[j] = (
            0.30 * row.iloc[j - 1] +
            0.40 * row.iloc[j] +
            0.30 * row.iloc[j + 1]
        )

    df.loc[i, pe_cols] = smooth

df.to_csv(
    "filled_dataset_time_strike_v3.csv",
    index=False
)

print("Saved -> filled_dataset_time_strike_v3.csv")