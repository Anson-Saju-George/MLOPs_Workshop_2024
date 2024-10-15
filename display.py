import json

# Load data from JSON file
def load_data(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Display all customers
def display_all_customers(filename):
    data = load_data(filename)
    if not data:
        print("No customers found.")
    else:
        for customer in data:
            print(f"Name: {customer['Name']}")
            print(f"Phone Number: {customer['Phone_Number']}")
            print(f"Address: {customer['Address']}")
            print(f"DoB: {customer['DoB']}")
            print(f"Email: {customer['Email']}\n")
