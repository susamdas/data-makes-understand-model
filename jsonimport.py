import json

customer_data = {
    "branch": "Grameen Bank - Dhaka",
    "customers": [{"name": "Susam", "loan_dbt":50000, "active": True},
                  {"name": "Rupa", "loan_dbt":60000, "active": True}
    ]
}
#Write
with open("customers.json", "w") as file:
    json.dump(customer_data, file, indent = 4)
#Read
with open("customers.json", "r") as file:
    data = json.load(file)
    print(data["branch"])
    print(data["customers"])
