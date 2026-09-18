import csv
import json
'''
branch_loans_data = [
    ["name","district","loan_amount_bdt","active"],
    ["Susam","Bhola","70000","active"],
    ["Rupa","Bhola","80000","active"],
    ["Arun","Bhola","60000","active"],
    ["Mehedi","Khulna","40000","active"],
    ["Emon","Barishal","70000","active"]
]
#write
with open("branch_loans_data.csv", "w", newline = "") as file:
    writer = csv.writer(file)
    writer.writerows(branch_loans_data)
#Read 
'''
with open("branch_loans_data.csv", "r") as file:
    reader = csv.DictReader(file)
    rows = list(reader)
    print("Customer above 30000bdt Loans are:")
    for row in rows:
        if int(row["loan_amount_bdt"])>30000:
            print(row["loan_amount_bdt"])
    total_loan =  sum(int(row["loan_amount_bdt"]) for row in rows)      
    print(f" Total Loan: {total_loan}")  

#Convert your loan data into a JSON file
for row in rows:
    row["loan_amount_bdt"] = int(row["loan_amount_bdt"])
output_data = {
    "branch": "Grameen Bank - Bhola",
    "customers": rows
}                     
#write
with open("branch_loans.json", "w") as file:
    json.dump(output_data, file, indent = 4)
print("file created!")
#read
with open("branch_loans.json", "r") as file:
    data = json.load(file)
    print(data["branch"])
    print(data["customers"])    