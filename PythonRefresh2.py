import csv

# Writing a CSV file
loan_data = [
    ["name", "district", "loan_amount_bdt", "active"],
    ["Rahim", "Dhaka", 50000, "True"],
    ["Karim", "Rangpur", 25000, "False"],
    ["Nasrin", "Bogura", 75000, "True"],
    ["Jamal", "Sylhet", 15000, "True"]
]
'''
with open("loans.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(loan_data)

print("File created!") '''

with open("loans.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)