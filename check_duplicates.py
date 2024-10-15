# Check if entry is a duplicate based on Phone Number or Email
def is_duplicate(new_entry, data):
    for customer in data:
        if customer["Phone_Number"] == new_entry["Phone_Number"] or customer["Email"] == new_entry["Email"]:
            return True
    return False
