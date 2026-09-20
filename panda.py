'''
import pandas as pd
df = pd.read_csv("branch_loans_data.csv")
df[df["loan_amount_bdt"] > 30000]
df["loan_amount_bdt"].sum()
df["loan_amount_bdt"].mean()'''


import pandas as pd

df = pd.read_csv("branch_loans_data.csv")

above_30k = df[df["loan_amount_bdt"] > 30000]
print(above_30k)

total = df["loan_amount_bdt"].sum()
print("Total:", total)

average = df["loan_amount_bdt"].mean()
print("Average:", average)