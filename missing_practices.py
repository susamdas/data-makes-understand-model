import pandas as pd
import numpy as np

data = {
    "name": ["Susam", "Rupa", "Arun", "Mehedi", "Emon", "Rupa"],
    "district": ["Bhola", "Bhola", None, "Khulna", "Barishal", "Bhola"],
    "loan_amount_bdt": [70000, 80000, 60000, None, 70000, 80000],
    "active": ["active", "active", "active", "inactive", "active", "active"]
}

df = pd.DataFrame(data)
print(df)
print(df.isnull())
print(df.isnull().sum())
df["district"] = df[ "district"].fillna("Unknown")
df["loan_amount_bdt"] = df["loan_amount_bdt"].fillna(df["loan_amount_bdt"].mean())
print(df)
print(df.duplicated())
df = df.drop_duplicates()
print(df)
df["loan_amount_bdt"] = df["loan_amount_bdt"].astype(int)
print(df)
print(df.dtypes)