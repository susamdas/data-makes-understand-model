import json

row = {
    "branch": "Grameen Bank - Dhaka",
    "customers": [{"name": "Susam", "loan_dbt":50000, "active": True},
                  {"name": "Rupa", "loan_dbt":60000, "active": True}
    ]
}
output_data = {
    "branch": "Grameen Bank - Bhola",
    "customers": row
}
#write
with open("branch_loan.json", "w") as file:
    json.dump(output_data, file, indent = 4)
print("Json file created!")
#Read
with open("branch_loan.json", "r") as file:
    data = json.load(file)
    print(data["branch"])
    print(data["customers"])