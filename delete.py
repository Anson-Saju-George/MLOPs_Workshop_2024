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

# Delete customer function
def delete_customer(filename, phone_number):
    data = load_data(filename)
    for customer in data:
        if customer["Phone_Number"] == phone_number:
            data.remove(customer)
            save_data(filename, data)
            print("Customer deleted successfully.")
            return
    print("Customer with this phone number not found.")
