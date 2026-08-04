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

    # Orders table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        order_id TEXT PRIMARY KEY,
        customer_id TEXT NOT NULL,
        product_id TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        order_date TEXT NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
        FOREIGN KEY (product_id) REFERENCES products(product_id)
    )
    """)

    connection.commit()
    connection.close()


def save_product(product):
    connection = sqlite3.connect("shophub.db")
    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO products (
        product_id,
        name,
        category,
        cost_price,
        selling_price,
        quantity,
        date_added,
        product_status
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        product.product_id,
        product.name,
        product.category,
        product.cost_price,
        product.selling_price,
        product.quantity,
        product.date_added,
        product.product_status
    ))

    connection.commit()
    connection.close()


def save_customer(customer):
    connection = sqlite3.connect("shophub.db")
    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO customers (
        customer_id,
        full_name,
        email,
        phone_number,
        address,
        registration_date
    )
    VALUES (?, ?, ?, ?, ?, ?)
    """, (
        customer.customer_id,
        customer.full_name,
        customer.email,
        customer.phone_number,
        customer.address,
        customer.registration_date
    ))

    connection.commit()
    connection.close()



def customer_exists(phone_number):
    connection = sqlite3.connect("shophub.db")
    cursor = connection.cursor()

    cursor.execute("""
    SELECT * FROM customers
    WHERE phone_number = ?
    """, (phone_number,))

    customer = cursor.fetchone()

    connection.close()

    if customer:
        return True
    else:
        return False