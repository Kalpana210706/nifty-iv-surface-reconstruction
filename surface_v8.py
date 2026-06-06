import pandas as pd

# Load best dataset
df = pd.read_csv("filled_dataset_surface_v6.csv")

option_cols = [c for c in df.columns if c not in ["datetime", "underlying_price"]]

ce_cols = sorted([c for c in option_cols if c.endswith("CE")])
pe_cols = sorted([c for c in option_cols if c.endswith("PE")])


def smooth_group(cols):
    for i in range(1, len(cols)-1):
        left = cols[i-1]
        curr = cols[i]
        right = cols[i+1]

        df[curr] = (
            0.25 * df[left]
            + 0.50 * df[curr]
            + 0.25 * df[right]
        )


smooth_group(ce_cols)
smooth_group(pe_cols)

df.to_csv("filled_dataset_surface_v8.csv", index=False)

print("Saved -> filled_dataset_surface_v8.csv")