import append
import update
import display
import delete
import check_duplicates

# Menu-driven program
def main():
    filename = "Data.json"

    while True:
        print("\nMenu:")
        print("1. Add new customer")
        print("2. Update customer details")
        print("3. Show all customers")
        print("4. Delete customer")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            address = input("Enter address: ")
            dob = input("Enter date of birth (DD/MM/YYYY): ")
            email = input("Enter email: ")

            new_entry = {
                "Name": name,
                "Phone_Number": phone,
                "Address": address,
                "DoB": dob,
                "Email": email
            }

            append.append_data(filename, new_entry)

        elif choice == "2":
            phone = input("Enter phone number of the customer to update: ")
            update.update_customer(filename, phone)

        elif choice == "3":
            display.display_all_customers(filename)

        elif choice == "4":
            phone = input("Enter phone number of the customer to delete: ")
            delete.delete_customer(filename, phone)

        elif choice == "5":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
