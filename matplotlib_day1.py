import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("branch_loans_data.csv")

'''
# Simple bar chart
plt.bar(df["name"], df["loan_amount_bdt"])
plt.xlabel("Customer")
plt.ylabel("Loan Amount (BDT)")
plt.title("Loan Amount by Customer")
plt.show()'''
'''
# Histogram — shows DISTRIBUTION of one numeric column
plt.hist(df["loan_amount_bdt"], bins=5)
plt.title("Loan Amount Distribution")
plt.show()

# Boxplot — shows spread + outliers
plt.boxplot(df["loan_amount_bdt"])
plt.title("Loan Amount Spread")
plt.show()

# Scatter plot — relationship between TWO numeric variables
plt.scatter(df["loan_amount_bdt"], df.index)
plt.show()'''

# Bar chart by district (auto-aggregates!)
sns.barplot(data=df, x="district", y="loan_amount_bdt")
plt.title("Average Loan by District")
plt.show()

# Distribution with a smooth curve
sns.histplot(df["loan_amount_bdt"], kde=True)
plt.show()

# Boxplot by category — great for comparing groups
sns.boxplot(data=df, x="district", y="loan_amount_bdt")
plt.show()