import sqlite3
from datetime import datetime


def create_tables():
    connection = sqlite3.connect("shophub.db")
    cursor = connection.cursor()

    # Products table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
    product_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL,
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
    email TEXT UNIQUE NOT NULL,
    phone_number TEXT UNIQUE NOT NULL,
    address TEXT NOT NULL,
    password TEXT NOT NULL,
    registration_date TEXT NOT NULL
)
    """)

    # Orders table
    cursor.execute("""
    
    CREATE TABLE IF NOT EXISTS orders (
    order_id TEXT PRIMARY KEY,
    customer_id TEXT NOT NULL,
    subtotal REAL NOT NULL,
    discount REAL NOT NULL,
    final_amount REAL NOT NULL,
    order_date TEXT NOT NULL,
    status TEXT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
)
    """)

    #Order Items table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS order_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id TEXT NOT NULL,
    product_id TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    unit_price REAL NOT NULL,
    subtotal REAL NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
)""")


    #Cart table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS carts (
    cart_id TEXT PRIMARY KEY,
    customer_id TEXT NOT NULL,
    created_at TEXT NOT NULL,
    status TEXT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
)
""")
    
    #Cart Items table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cart_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cart_id TEXT NOT NULL,
    product_id TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    FOREIGN KEY (cart_id) REFERENCES carts(cart_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
)
    """)

    #Payments table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS payments (
    payment_id TEXT PRIMARY KEY,
    order_id TEXT NOT NULL,
    amount REAL NOT NULL,
    payment_method TEXT NOT NULL,
    payment_date TEXT NOT NULL,
    status TEXT NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
)
    """)

    #Discounts table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS discounts (
    discount_id TEXT PRIMARY KEY,
    discount_name TEXT NOT NULL,
    percentage REAL NOT NULL,
    start_date TEXT NOT NULL,
    end_date TEXT NOT NULL,
    status TEXT NOT NULL
)

    """)


    #Admin Authentication table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS admins (
    admin_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
    """)

    connection.commit()
    connection.close()



def generate_customer_id():
    connection = sqlite3.connect("shophub.db")
    cursor = connection.cursor()

    cursor.execute("""
    SELECT customer_id
    FROM customers
    ORDER BY customer_id DESC
    LIMIT 1
    """)

    result = cursor.fetchone()

    connection.close()

    if result is None:
        return "CUST001"

    last_id = result[0]
    number = int(last_id.replace("CUST", ""))
    new_number = number + 1

    return f"CUST{new_number:03d}"


def generate_product_id():
    connection = sqlite3.connect("shophub.db")
    cursor = connection.cursor()

    cursor.execute("""
    SELECT product_id
    FROM products
    ORDER BY product_id DESC
    LIMIT 1
    """)

    result = cursor.fetchone()
    connection.close()

    if result is None:
        return "PROD001"

    last_id = result[0]
    number = int(last_id.replace("PROD", ""))
    new_number = number + 1

    return f"PROD{new_number:03d}"


def generate_cart_id():
    connection = sqlite3.connect("shophub.db")
    cursor = connection.cursor()

    cursor.execute("""
    SELECT cart_id
    FROM carts
    ORDER BY cart_id DESC
    LIMIT 1
    """)

    result = cursor.fetchone()
    connection.close()

    if result is None:
        return "CART001"

    last_id = result[0]
    number = int(last_id.replace("CART", ""))
    new_number = number + 1

    return f"CART{new_number:03d}"


def generate_order_id():
    connection = sqlite3.connect("shophub.db")
    cursor = connection.cursor()

    cursor.execute("""
    SELECT order_id
    FROM orders
    ORDER BY order_id DESC
    LIMIT 1
    """)

    result = cursor.fetchone()
    connection.close()

    if result is None:
        return "ORD0001"

    last_id = result[0]
    number = int(last_id.replace("ORD", ""))
    new_number = number + 1

    return f"ORD{new_number:04d}"


def generate_payment_id():
    connection = sqlite3.connect("shophub.db")
    cursor = connection.cursor()

    cursor.execute("""
    SELECT payment_id
    FROM payments
    ORDER BY payment_id DESC
    LIMIT 1
    """)

    result = cursor.fetchone()
    connection.close()

    if result is None:
        return "PAY0001"

    last_id = result[0]
    number = int(last_id.replace("PAY", ""))
    new_number = number + 1

    return f"PAY{new_number:04d}"




def generate_discount_id():
    connection = sqlite3.connect("shophub.db")
    cursor = connection.cursor()

    cursor.execute("""
    SELECT discount_id
    FROM discounts
    ORDER BY discount_id DESC
    LIMIT 1
    """)

    result = cursor.fetchone()
    connection.close()

    if result is None:
        return "DISC001"

    last_id = result[0]
    number = int(last_id.replace("DISC", ""))
    new_number = number + 1

    return f"DISC{new_number:03d}"



def get_current_date():
    return datetime.now().strftime("%Y-%m-%d")



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
        password,
        registration_date
    )
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        customer.customer_id,
        customer.full_name,
        customer.email,
        customer.phone_number,
        customer.address,
        customer.password,
        customer.registration_date
    ))

    connection.commit()
    connection.close()



def authenticate_customer(email, password):
    connection = sqlite3.connect("shophub.db")
    cursor = connection.cursor()

    cursor.execute("""
    SELECT customer_id
    FROM customers
    WHERE email = ? AND password = ?
    """, (email, password))

    result = cursor.fetchone()

    connection.close()

    if result is not None:
        return result[0]
    else:
        return None


def get_customer(customer_id):
    connection = sqlite3.connect("shophub.db")
    cursor = connection.cursor()

    cursor.execute("""
    SELECT customer_id, full_name, email, phone_number, address
    FROM customers
    WHERE customer_id = ?
    """, (customer_id,))

    result = cursor.fetchone()

    connection.close()

    return result



def create_admin():
    connection = sqlite3.connect("shophub.db")
    cursor = connection.cursor()

    cursor.execute("""
    SELECT admin_id
    FROM admins
    WHERE username = ?
    """, ("admin",))

    existing_admin = cursor.fetchone()

    if existing_admin is None:
        cursor.execute("""
        INSERT INTO admins (username, password)
        VALUES (?, ?)
        """, ("admin", "admin123"))

        connection.commit()

    connection.close()



def authenticate_admin(username, password):
    connection = sqlite3.connect("shophub.db")
    cursor = connection.cursor()

    cursor.execute("""
    SELECT admin_id
    FROM admins
    WHERE username = ? AND password = ?
    """, (username, password))

    result = cursor.fetchone()

    connection.close()

    if result is not None:
        return result[0]
    else:
        return None



def save_product(product):
    connection = sqlite3.connect("shophub.db")
    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO products (
        product_id,
        name,
        category,
        price,
        quantity,
        date_added,
        product_status
    )
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        product.product_id,
        product.name,
        product.category,
        product.price,
        product.quantity,
        product.date_added,
        product.product_status
    ))

    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect("shophub.db")
    cursor = connection.cursor()

    cursor.execute("""
    SELECT product_id, name, category, price, quantity, date_added, product_status
    FROM products
    ORDER BY product_id
    """)

    products = cursor.fetchall()

    connection.close()

    return products


































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

def get_customer_id(phone_number):
    connection = sqlite3.connect("shophub.db")
    cursor = connection.cursor()

    cursor.execute("""
    SELECT customer_id FROM customers
    WHERE phone_number = ?
    """, (phone_number,))

    result = cursor.fetchone()

    connection.close()

    if result is not None:
        return result[0]
    else:
        return None
    
    connection.close()                                                                   


def get_customer_name(customer_id):
    connection = sqlite3.connect("shophub.db")
    cursor = connection.cursor()

    cursor.execute("""
    SELECT full_name FROM customers
    WHERE customer_id = ?
    """, (customer_id,))

    result = cursor.fetchone()

    connection.close()

    if result is not None:
        return result[0]
    else:
        return None
    
    connection.close()

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
    
    connection.close()



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

    
    connection.close()


def save_order(order):
    connection = sqlite3.connect("shophub.db")
    cursor = connection.cursor()

    try:
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
        return True

    except sqlite3.IntegrityError:
        print("\n❌ Order ID already exists.")
        print("Please enter a different Order ID.")
        return False

    finally:
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
    connection.commit()
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

def get_product_name(product_id):
    connection = sqlite3.connect("shophub.db")
    cursor = connection.cursor()

    cursor.execute("""
    SELECT name FROM products
    WHERE product_id = ?
    """, (product_id,))

    result = cursor.fetchone()

    connection.close()

    if result is not None:
        return result[0]
    else:
        return None


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