import database
import customer
import customer_auth
import admin_auth
import admin


def main_menu():

    while True:

        print("\n========== SHOPHUB ==========")
        print("1. Customer Sign Up")
        print("2. Customer Login")
        print("3. Admin Login")
        print("0. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            customer_auth.customer_signup()

        elif choice == "2":

            customer_data = customer_auth.customer_login()

            if customer_data is not None:
                customer.customer_menu(customer_data)

        elif choice == "3":

            admin_id = admin_auth.admin_login()

            if admin_id is not None:
                admin.admin_menu()
        
        elif choice == "0":

            print("\nThank you for using ShopHub!")
            break

        else:

            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":

    database.create_tables()
    database.create_admin()

    main_menu()