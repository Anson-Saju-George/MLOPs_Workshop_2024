# MLOPs_Workshop_2024
# Customer Management System - Workshop Project
Customer Management System - MLOps Workshop Project
This project is a menu-driven Python application designed for managing customer data. It supports appending, updating, displaying, and deleting customer records while checking for duplicates based on phone number and email. The program is modular, with separate Python files handling individual functionalities.

## Project Structure  
Project directory/  

 │  
 ├── Data.json               # JSON file to store customer data  
 ├── main.py                 # Main menu-driven program  
 ├── append.py               # Module to append new customers  
 ├── update.py               # Module to update customer details  
 ├── display.py              # Module to display all customers  
 ├── delete.py               # Module to delete customers  
 └── check_duplicates.py     # Module to check for duplicate customers  
## Features  
Add Customer: Allows you to add new customer details. Duplicate entries (same phone number or email) are not allowed.  
Update Customer: Update the details of an existing customer based on their phone number.  
Display Customers: Display all customer details in the system.  
Delete Customer: Delete a customer from the system based on their phone number.  
Duplicate Check: Automatically checks for duplicate entries based on phone number and email.  
Prerequisites  
Python 3.x installed on your system.  

## Running the Program
Execute the main.py file to start the program:  
python main.py  
You will be presented with a menu:  

Menu:
1. Add new customer
2. Update customer details
3. Show all customers
4. Delete customer
5. Exit

## Module Details
- append.py: Handles adding new customers and checks for duplicates using check_duplicates.py.
- update.py: Updates existing customer details based on phone number.
- display.py: Displays all customer records from the Data.json file.
- delete.py: Deletes a customer record by phone number.
- check_duplicates.py: Checks for duplicate entries based on phone number or email.

## Contribution
Feel free to contribute to this project by opening issues or submitting pull requests.

## License
This project is not licensed under any organisation - see the LICENSE file for details.  
