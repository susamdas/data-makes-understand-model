import pandas as pd
import scipy.stats as stats
import numpy as np 


df = pd.read_csv("branch_loans_data.csv")
print(df["loan_amount_bdt"].mean())
print(df["loan_amount_bdt"].std())
print(df["loan_amount_bdt"].median())

dhaka_loans = df[df["district"] == "Dhaka"]["loan_amount_bdt"]
khulna_loans = df[df["district"] == "Khulna"]["loan_amount_bdt"]

t_stat, p_value = stats.ttest_ind(dhaka_loans, khulna_loans)
print(f"T-statistic: {t_stat}")
print(f"P-value: {p_value}")


data = df["loan_amount_bdt"]
mean = np.mean(data)
sem = stats.sem(data)  # standard error of the mean
ci = stats.t.interval(confidence=0.95, df=len(data)-1, loc=mean, scale=sem)
print(f"Mean: {mean}")
print(f"95% Confidence Interval: {ci}")