# %% import pandas and read the csv file 
# modify the path if needed
import pandas as pd

df = pd.read_csv('../Lab 2/Resources/rectangles_data.csv')
df["area"] = df['length'] * df['width']


# %%
summary = [
    ("Total Count", df["area"].shape[0]),
    ("Total Area", df["area"].sum()),
    ("Average Area",df["area"].mean()),
    ("Maximum Area",max(df["area"])),
    ("Minimum Area", min(df["area"])),
]

for key, value in summary:
    print(f"{key}: {str(value)}")

# %%
d = pd.DataFrame(summary)
file_path = "Activity1/summary.csv"
d.to_csv(file_path, index=[0])
