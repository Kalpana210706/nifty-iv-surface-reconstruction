import pandas as pd

v6 = pd.read_csv("filled_dataset_surface_v6.csv")
cubic = pd.read_csv("filled_dataset_cubic.csv")

cols = [c for c in v6.columns if c not in ["datetime","underlying_price"]]

out = v6.copy()

for col in cols:
    out[col] = (
        0.90 * v6[col]
        + 0.10 * cubic[col]
    )

out.to_csv("filled_dataset_blend_90_10.csv", index=False)

print("Saved")