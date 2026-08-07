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
    subtotal REAL NOT NULL,
    final_amount REAL NOT NULL,
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

    if customer is not None:
        return True
    else:
        return False


def product_exists(product_id):
    connection = sqlite3.connect("shophub.db")
    cursor = connection.cursor()

    cursor.execute("""
    SELECT * FROM products
    WHERE product_id = ?
    """, (product_id,))

    product = cursor.fetchone()

    connection.close()

    if product is not None:
        return True
    else:
        return False


def get_product_quantity(product_id):
    connection = sqlite3.connect("shophub.db")
    cursor = connection.cursor()

    cursor.execute("""
    SELECT quantity FROM products
    WHERE product_id = ?
    """, (product_id,))

    result = cursor.fetchone()
    connection.close()

    if result is not None:
        return result[0]
    else:
        return 0



def get_selling_price(product_id):
    connection = sqlite3.connect("shophub.db")
    cursor = connection.cursor()

    cursor.execute("""
    SELECT selling_price
    FROM products
    WHERE product_id = ?
    """, (product_id,))

    result = cursor.fetchone()

    connection.close()

    if result is not None:
        return result[0]
    else:
        return 0


def save_order(order):
    connection = sqlite3.connect("shophub.db")
    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO orders (
        order_id,
        customer_id,
        product_id,
        quantity,
        subtotal,
        final_amount,
        order_date
    )
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        order.order_id,
        order.customer_id,
        order.product_id,
        order.quantity,
        order.calculate_subtotal(),
        order.calculate_final_amount(),
        order.order_date
    ))

    connection.commit()
    connection.close()



def update_product_quantity(product_id, new_quantity):
    connection = sqlite3.connect("shophub.db")
    cursor = connection.cursor()

    cursor.execute("""
    UPDATE products
    SET quantity = ?
    WHERE product_id = ?
    """, (new_quantity, product_id))

    connection.commit()
    connection.close() 

def get_total_sales():
    connection = sqlite3.connect("shophub.db")
    cursor = connection.cursor()

    cursor.execute("""
    SELECT SUM(quantity)
    FROM orders
    """)

    result = cursor.fetchone()

    connection.close()

    return result[0]




def get_total_revenue():
    connection = sqlite3.connect("shophub.db")
    cursor = connection.cursor()

    cursor.execute("""
    SELECT SUM(final_amount)
    FROM orders
    """)

    result = cursor.fetchone()

    connection.close()

    if result[0] is not None:
        return result[0]
    else:
        return 0


def get_low_stock():
    connection = sqlite3.connect("shophub.db")
    cursor = connection.cursor()

    cursor.execute("""
    SELECT * FROM products
    WHERE quantity < 5
    """)

    low_stock_products = cursor.fetchall()

    connection.close()

    return low_stock_products

def get_best_selling_products():
    connection = sqlite3.connect("shophub.db")
    cursor = connection.cursor()

    cursor.execute("""
    SELECT product_id, SUM(quantity)
    FROM orders
    GROUP BY product_id
    ORDER BY SUM(quantity) DESC
    """)

    best_selling_products = cursor.fetchall()

    connection.close()

    return best_selling_products


def get_most_valuable_customers():
    connection = sqlite3.connect("shophub.db")
    cursor = connection.cursor()

    cursor.execute("""
    SELECT customer_id, SUM(final_amount)
    FROM orders
    GROUP BY customer_id
    ORDER BY SUM(final_amount) DESC
    """)

    most_valuable_customers = cursor.fetchall()

    connection.close()

    return most_valuable_customers


create_tables()