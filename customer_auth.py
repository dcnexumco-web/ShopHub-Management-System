import customer
import database
import validators



def customer_signup():

    print("\n========== CUSTOMER SIGN UP ==========")

    full_name = input("Enter your full name: ")

    email = input("Enter your email: ")

    while not validators.validate_email(email):
        print("Invalid email address.")
        email = input("Enter your email: ")

    phone_number = input("Enter your phone number: ")

    while not validators.validate_phone_number(phone_number):
        print("Invalid phone number.")
        phone_number = input("Enter your phone number: ")

    address = input("Enter your address: ")

    
    password = input("Create a password: ")
    

    while not validators.validate_password(password):
        print("Password must be at least 6 characters.")
        password = input("Create a password: ")
    confirm_password = input("Confirm password: ")

    while password != confirm_password:
        print("Passwords do not match.")
        password = input("Create a password: ")
        confirm_password = input("Confirm password: ")

    customer_id = database.generate_customer_id()

    registration_date = database.get_current_date()

    new_customer = customer.Customer(
        customer_id,
        full_name,
        email,
        phone_number,
        address,
        password,
        registration_date
    )
    try:
        database.save_customer(new_customer)

    except sqlite3.IntegrityError:
        print("❌ An account with that email or phone number already exists.")
        return

    except sqlite3.Error:
        print("❌ A database error occurred. Please try again.")
        return

    print("\n✅ Account created successfully!")
    print(f"Your Customer ID is: {customer_id}")


def customer_login():

    print("\n========== CUSTOMER LOGIN ==========")


    email = input("Enter your email: ")

    while not validators.validate_email(email):
        print("Invalid email address.")
        email = input("Enter your email: ")
    
    password = input("Enter your password: ")


    customer_id = database.authenticate_customer(
        email,
        password
    )

    if customer_id is None:
        print("\n❌ Invalid email or password.")
        return None

    print("\n✅ Login successful!")

    customer_data = database.get_customer(customer_id)

    return customer_data


