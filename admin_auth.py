import database



def admin_login():

    print("\n========== ADMIN LOGIN ==========")

    username = input("Enter username: ")
    password = input("Enter password: ")

    admin_id = database.authenticate_admin(
        username,
        password
    )

    if admin_id is None:
        print("\n❌ Invalid username or password.")
        return None

    print("\n✅ Admin login successful!")

    return admin_id