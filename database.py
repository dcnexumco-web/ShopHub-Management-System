import sqlite3

def create_tables():
    connection = sqlite3.connect("shophub.db")
    cursor = connection.cursor()

    # Products table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        product_id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        cost_price REAL NOT NULL,
        selling_price REAL NOT NULL,
        quantity INTEGER NOT NULL,
        date_added TEXT NOT NULL,
        product_status TEXT NOT NULL
    )
    """)

    # Customers table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        customer_id TEXT PRIMARY KEY,
        full_name TEXT NOT NULL,
        email TEXT NOT NULL,
        phone_number TEXT NOT NULL,
        address TEXT NOT NULL,
        registration_date TEXT NOT NULL
    )
    """)

    connection.commit()
    connection.close()