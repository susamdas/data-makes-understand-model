import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)  # makes random numbers reproducible

names = ["Susam", "Rupa", "Arun", "Mehedi", "Emon", "Karim", "Nasrin", "Jamal",
         "Fatima", "Rahim", "Sultana", "Habib", "Ayesha", "Kamal", "Rina",
         "Salma", "Faruk", "Nasir", "Rumana", "Alam"]

districts = ["Bhola", "Khulna", "Barishal", "Dhaka", "Rangpur"]

data = {
    "name": names,
    "district": np.random.choice(districts, size=20),
    "loan_amount_bdt": np.random.randint(10000, 100000, size=20),
    "active": np.random.choice(["active", "inactive"], size=20, p=[0.8, 0.2])
}

df = pd.DataFrame(data)
#print(df)
print(df.info())
print(df.describe())
#Add a new column loan_category — "High" if above 60000 else "Low" (you already know this from Day 4)
df["loan_category"] = df["loan_amount_bdt"].apply(lambda x: "High" if x>60000 else "Low")
print(df)
#Aggregate: Find total and average loan amount per district
print(df.groupby("district")["loan_amount_bdt"].agg(["sum", "mean"]).round(2))
#Visualize (make all 3):
#A bar chart showing average loan amount per district (Seaborn)
#A histogram of loan amount distribution
#A boxplot comparing loan amounts across districts
avg_loan_amount = df.groupby("district")["loan_amount_bdt"].mean().round(2)
#print(avg_loan_amount)
sns.barplot(x=avg_loan_amount.index, y=avg_loan_amount.values)
plt.title("Average Loan Amount per district")
plt.show()

sns.histplot(df["loan_amount_bdt"], kde =True)
plt.show()

sns.boxplot(data= df, x = df["district"], y = df["loan_amount_bdt"])
plt.show()