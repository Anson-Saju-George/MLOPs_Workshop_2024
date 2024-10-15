import json

# Load data from JSON file
def load_data(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save data to JSON file
def save_data(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

# Update customer details function
def update_customer(filename, phone_number):
    data = load_data(filename)
    for customer in data:
        if customer["Phone_Number"] == phone_number:
            print("Customer found.")
            customer["Name"] = input("Enter new name: ") or customer["Name"]
            customer["Address"] = input("Enter new address: ") or customer["Address"]
            customer["DoB"] = input("Enter new DoB (DD/MM/YYYY): ") or customer["DoB"]
            customer["Email"] = input("Enter new email: ") or customer["Email"]
            save_data(filename, data)
            print("Customer updated successfully.")
            return
    print("Customer with this phone number not found.")
