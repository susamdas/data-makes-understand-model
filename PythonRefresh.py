'''
age = 28              # int
balance = 15420.75    # float
name = "Rahim"         # string
is_active = True      # boolean

# List - ordered, changeable
loan_amounts = [5000, 12000, 8500, 20000]

# Dictionary - key-value pairs (very common in DS)
customer = {"name": "Rahim", "balance": 15420, "active": True}

# Tuple - ordered, unchangeable
coordinates = (23.8103, 90.4125)  # lat, long

# Basic loop

for amount in loan_amounts:
    if amount > 10000:
        print(f"Highest loan Amount: {amount}")
'''
# List comprehension (you'll use this A LOT in data science)
#high_value =[a for a in loan_amounts if a>10000]
#print(f"Highest Loan Amount: {high_value}")
#You have a list of loan amounts: [3000, 15000, 7500, 22000, 9800, 4500]
#Write a list comprehension that finds all loans above 10,000
#Write a function average_loan(loans) that returns the average
#Print: "X out of Y loans are high-value" 
loan_amounts = [3000, 15000, 7500, 22000, 9800, 4500]
highest_loan_Amounts = [a for a in loan_amounts if a>10000]
print(f"Hightest loans: {highest_loan_Amounts}")
def avg_loan(loans):
    total = sum(loans)
    count = len(loans)
    return total/count
result = avg_loan(loan_amounts)
print(f"Average Loan: {result}")

print(f"{len(highest_loan_Amounts)} out of {len(loan_amounts)} loans are high-value")