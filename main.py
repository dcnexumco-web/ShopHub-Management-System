import database
import customer
import customer_auth
import admin_auth
import admin


def login():

    print("\n========== LOGIN ==========")

    username_or_email = input("Enter your email: ")
    password = input("Enter password: ")

    # Check if admin
    admin_id = database.authenticate_admin(
        username_or_email,
        password
    )

    if admin_id is not None:
        print("\n✅ Admin login successful!")
        admin.admin_menu()
        return

    # Check if customer
    customer_id = database.authenticate_customer(
        username_or_email,
        password
    )

    if customer_id is not None:
        print("\n✅ Customer login successful!")

        customer_data = database.get_customer(customer_id)

        customer.customer_menu(customer_data)
        return

    print("\n❌ Invalid username/email or password.")


def main_menu():

    while True:

        print("\n========== SHOPHUB ==========")
        print("1. Login")
        print("2. Sign Up")
        print("0. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            login()

        elif choice == "2":

            customer_auth.customer_signup()

        elif choice == "0":

            print("\nThank you for using ShopHub!")
            break

        else:

            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":

    database.create_tables()
    database.create_admin()

    main_menu()