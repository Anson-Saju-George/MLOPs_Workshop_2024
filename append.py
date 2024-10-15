import json
import check_duplicates

# Load data from JSON file
def load_data(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # If file doesn't exist, return an empty list

# Save data to JSON file
def save_data(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

# Append data function
def append_data(filename, new_entry):
    data = load_data(filename)
    if check_duplicates.is_duplicate(new_entry, data):
        print("Duplicate entry (Phone Number or Email already exists). Not adding.")
    else:
        data.append(new_entry)
        save_data(filename, data)
        print("New entry added successfully.")
