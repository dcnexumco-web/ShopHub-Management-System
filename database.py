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
    connection = None

    try:
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

        return "success"

    except sqlite3.IntegrityError as e:
        print(f"Database constraint error: {e}")
        return "integrity_error"

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return "database_error"

    finally:
        if connection:
            connection.close()


def authenticate_customer(email, password):
    connection = None

    try:
        connection = sqlite3.connect("shophub.db")
        cursor = connection.cursor()

        cursor.execute("""
        SELECT customer_id
        FROM customers
        WHERE email = ? AND password = ?
        """, (email, password))

        result = cursor.fetchone()

        if result is not None:
            return result[0]
        else:
            return None

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None

    finally:
        if connection:
            connection.close()


def get_customer(customer_id):
    connection = None

    try:
        connection = sqlite3.connect("shophub.db")
        cursor = connection.cursor()

        cursor.execute("""
        SELECT customer_id, full_name, email, phone_number, address
        FROM customers
        WHERE customer_id = ?
        """, (customer_id,))

        return cursor.fetchone()

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None

    finally:
        if connection:
            connection.close()

def create_admin():
    connection = None

    try:
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

    except sqlite3.IntegrityError as e:
        print(f"Database constraint error: {e}")

    except sqlite3.Error as e:
        print(f"Database error: {e}")

    finally:
        if connection:
            connection.close()



def authenticate_admin(username, password):
    connection = None

    try:
        connection = sqlite3.connect("shophub.db")
        cursor = connection.cursor()

        cursor.execute("""
        SELECT admin_id
        FROM admins
        WHERE username = ? AND password = ?
        """, (username, password))

        result = cursor.fetchone()

        if result is not None:
            return result[0]
        else:
            return None

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None

    finally:
        if connection:
            connection.close()



def save_product(product):
    connection = None

    try:
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

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False

    finally:
        if connection is not None:
            connection.close()

    return True


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


def search_product(search_term):
    connection = sqlite3.connect("shophub.db")
    cursor = connection.cursor()

    cursor.execute("""
    SELECT product_id, name, category, price, quantity, date_added, product_status
    FROM products
    WHERE product_id = ?
       OR name LIKE ?
       OR category LIKE ?
    """, (
        search_term,
        f"%{search_term}%",
        f"%{search_term}%"
    ))

    products = cursor.fetchall()

    connection.close()

    return products




def update_product(product_id, name, category, price):
    connection = None

    try:
        connection = sqlite3.connect("shophub.db")
        cursor = connection.cursor()

        cursor.execute("""
        UPDATE products
        SET name = ?,
            category = ?,
            price = ?
        WHERE product_id = ?
        """, (
            name,
            category,
            price,
            product_id
        ))

        connection.commit()

        return cursor.rowcount

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return 0

    finally:
        if connection is not None:
            connection.close()



def delete_product(product_id):
    connection = None

    try:
        connection = sqlite3.connect("shophub.db")
        cursor = connection.cursor()

        cursor.execute("""
        DELETE FROM products
        WHERE product_id = ?
        """, (product_id,))

        connection.commit()

        return cursor.rowcount

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return 0

    finally:
        if connection is not None:
            connection.close()


def increase_stock(product_id, amount):
    connection = None

    try:
        connection = sqlite3.connect("shophub.db")
        cursor = connection.cursor()

        cursor.execute("""
        UPDATE products
        SET quantity = quantity + ?,
            product_status = 'Available'
        WHERE product_id = ?
        """, (amount, product_id))

        connection.commit()

        return cursor.rowcount

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return 0

    finally:
        if connection is not None:
            connection.close()

def reduce_stock(product_id, amount):
    connection = None

    try:
        connection = sqlite3.connect("shophub.db")
        cursor = connection.cursor()

        cursor.execute("""
        SELECT quantity
        FROM products
        WHERE product_id = ?
        """, (product_id,))

        result = cursor.fetchone()

        if result is None:
            return "not_found"

        current_quantity = result[0]

        if amount > current_quantity:
            return "insufficient"

        new_quantity = current_quantity - amount

        if new_quantity == 0:
            status = "Out of Stock"
        else:
            status = "Available"

        cursor.execute("""
        UPDATE products
        SET quantity = ?,
            product_status = ?
        WHERE product_id = ?
        """, (
            new_quantity,
            status,
            product_id
        ))

        connection.commit()

        return "success"

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return "database_error"

    finally:
        if connection is not None:
            connection.close()

def create_cart(customer_id):
    connection = None

    try:
        cart_id = generate_cart_id()
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        connection = sqlite3.connect("shophub.db")
        cursor = connection.cursor()

        cursor.execute("""
        INSERT INTO carts (
            cart_id,
            customer_id,
            created_at,
            status
        )
        VALUES (?, ?, ?, ?)
        """, (
            cart_id,
            customer_id,
            created_at,
            "Active"
        ))

        connection.commit()

        return cart_id

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None

    finally:
        if connection is not None:
            connection.close()


def get_active_cart(customer_id):
    connection = sqlite3.connect("shophub.db")
    cursor = connection.cursor()

    cursor.execute("""
    SELECT cart_id
    FROM carts
    WHERE customer_id = ? AND status = ?
    """, (customer_id, "Active"))

    result = cursor.fetchone()

    connection.close()

    if result is not None:
        return result[0]
    else:
        return None




def add_to_cart(cart_id, product_id, quantity):
    connection = None

    try:
        connection = sqlite3.connect("shophub.db")
        cursor = connection.cursor()

        cursor.execute("""
        SELECT price, quantity
        FROM products
        WHERE product_id = ?
        """, (product_id,))

        product = cursor.fetchone()

        if product is None:
            return "not_found"

        price = product[0]
        stock = product[1]

        if quantity <= 0:
            return "invalid_quantity"

        if quantity > stock:
            return "insufficient"

        cursor.execute("""
        SELECT quantity
        FROM cart_items
        WHERE cart_id = ? AND product_id = ?
        """, (cart_id, product_id))

        existing_item = cursor.fetchone()

        if existing_item is not None:
            new_quantity = existing_item[0] + quantity

            if new_quantity > stock:
                return "insufficient"

            cursor.execute("""
            UPDATE cart_items
            SET quantity = ?
            WHERE cart_id = ? AND product_id = ?
            """, (new_quantity, cart_id, product_id))

        else:
            cursor.execute("""
            INSERT INTO cart_items (
                cart_id,
                product_id,
                quantity
            )
            VALUES (?, ?, ?)
            """, (cart_id, product_id, quantity))

        connection.commit()

        return "success"

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return "database_error"

    finally:
        if connection is not None:
            connection.close()



def get_cart_items(cart_id):

    connection = sqlite3.connect("shophub.db")
    cursor = connection.cursor()

    cursor.execute("""
    SELECT
        cart_items.product_id,
        products.name,
        products.price,
        cart_items.quantity,
        products.price * cart_items.quantity
    FROM cart_items
    JOIN products
    ON cart_items.product_id = products.product_id
    WHERE cart_items.cart_id = ?
    """, (cart_id,))

    items = cursor.fetchall()

    connection.close()

    return items




def update_cart_item(cart_id, product_id, quantity):
    connection = None

    try:
        connection = sqlite3.connect("shophub.db")
        cursor = connection.cursor()

        if quantity <= 0:
            connection.close()
            return "invalid_quantity"

        cursor.execute("""
        SELECT quantity
        FROM products
        WHERE product_id = ?
        """, (product_id,))

        product = cursor.fetchone()

        if product is None:
            connection.close()
            return "not_found"

        stock = product[0]

        if quantity > stock:
            connection.close()
            return "insufficient"

        cursor.execute("""
        UPDATE cart_items
        SET quantity = ?
        WHERE cart_id = ? AND product_id = ?
        """, (quantity, cart_id, product_id))

        connection.commit()

        return "success"


    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return "database_error"

    finally:
        if connection is not None:
            connection.close()



def remove_from_cart(cart_id, product_id):
    connection = None

    try:
        connection = sqlite3.connect("shophub.db")
        cursor = connection.cursor()

        cursor.execute("""
        DELETE FROM cart_items
        WHERE cart_id = ? AND product_id = ?
        """, (cart_id, product_id))

        connection.commit()

        if cursor.rowcount == 0:
            return "not_found"

        return "success"

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return "database_error"

    finally:
        if connection is not None:
            connection.close()



def get_cart_total(cart_id):

    connection = sqlite3.connect("shophub.db")
    cursor = connection.cursor()

    cursor.execute("""
    SELECT SUM(products.price * cart_items.quantity)
    FROM cart_items
    JOIN products
    ON cart_items.product_id = products.product_id
    WHERE cart_items.cart_id = ?
    """, (cart_id,))

    result = cursor.fetchone()

    connection.close()

    if result[0] is None:
        return 0

    return result[0]



def create_order(customer_id, subtotal, discount, final_amount):
    connection = None

    try:
        order_id = generate_order_id()
        order_date = get_current_date()

        connection = sqlite3.connect("shophub.db")
        cursor = connection.cursor()

        cursor.execute("""
        INSERT INTO orders (
            order_id,
            customer_id,
            subtotal,
            discount,
            final_amount,
            order_date,
            status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            order_id,
            customer_id,
            subtotal,
            discount,
            final_amount,
            order_date,
            "Pending Payment"
        ))

        connection.commit()

        return order_id

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None

    finally:
        if connection is not None:
            connection.close()



def save_order_items(order_id, cart_id):
    connection = None

    try:
        connection = sqlite3.connect("shophub.db")
        cursor = connection.cursor()

        cursor.execute("""
        SELECT product_id, quantity
        FROM cart_items
        WHERE cart_id = ?
        """, (cart_id,))

        items = cursor.fetchall()

        for product_id, quantity in items:

            cursor.execute("""
            SELECT price
            FROM products
            WHERE product_id = ?
            """, (product_id,))

            price = cursor.fetchone()[0]

            subtotal = price * quantity

            cursor.execute("""
            INSERT INTO order_items (
                order_id,
                product_id,
                quantity,
                unit_price,
                subtotal
            )
            VALUES (?, ?, ?, ?, ?)
            """, (
                order_id,
                product_id,
                quantity,
                price,
                subtotal
            ))

        connection.commit()

        return True

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False

    finally:
        if connection is not None:
            connection.close()




def clear_cart(cart_id):
    connection = None

    try:
        connection = sqlite3.connect("shophub.db")
        cursor = connection.cursor()

        cursor.execute("""
        DELETE FROM cart_items
        WHERE cart_id = ?
        """, (cart_id,))

        cursor.execute("""
        UPDATE carts
        SET status = 'Completed'
        WHERE cart_id = ?
        """, (cart_id,))

        connection.commit()

        return True

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False

    finally:
        if connection is not None:
            connection.close()




    def save_payment(order_id, amount, payment_method):
        connection = None

        try:
            payment_id = generate_payment_id()
            payment_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            connection = sqlite3.connect("shophub.db")
            cursor = connection.cursor()

            cursor.execute("""
            INSERT INTO payments (
            payment_id,
            order_id,
            amount,
            payment_method,
            payment_date,
            status
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """, (
            payment_id,
            order_id,
            amount,
            payment_method,
            payment_date,
            "Successful"
            ))

            cursor.execute("""
            UPDATE orders
            SET status = 'Paid'
            WHERE order_id = ?
            """, (order_id,))

            connection.commit()

            return payment_id

        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None

        finally:
            if connection is not None:
                connection.close()



def get_order(order_id):

    connection = sqlite3.connect("shophub.db")
    cursor = connection.cursor()

    cursor.execute("""
    SELECT order_id, customer_id, subtotal, discount,
           final_amount, order_date, status
    FROM orders
    WHERE order_id = ?
    """, (order_id,))

    result = cursor.fetchone()

    connection.close()

    return result


def get_payment(order_id):

    connection = sqlite3.connect("shophub.db")
    cursor = connection.cursor()

    cursor.execute("""
    SELECT payment_id, amount, payment_method,
           payment_date, status
    FROM payments
    WHERE order_id = ?
    """, (order_id,))

    result = cursor.fetchone()

    connection.close()

    return result


def get_order_items(order_id):

    connection = sqlite3.connect("shophub.db")
    cursor = connection.cursor()

    cursor.execute("""
    SELECT products.name,
           order_items.quantity,
           order_items.unit_price,
           order_items.subtotal
    FROM order_items
    JOIN products
    ON order_items.product_id = products.product_id
    WHERE order_items.order_id = ?
    """, (order_id,))

    items = cursor.fetchall()

    connection.close()

    return items




def get_all_orders():

    connection = sqlite3.connect("shophub.db")
    cursor = connection.cursor()

    cursor.execute("""
    SELECT order_id, customer_id, subtotal,
           discount, final_amount, order_date, status
    FROM orders
    ORDER BY order_id
    """)

    orders = cursor.fetchall()

    connection.close()

    return orders


def get_all_payments():

    connection = sqlite3.connect("shophub.db")
    cursor = connection.cursor()

    cursor.execute("""
    SELECT payment_id, order_id, amount,
           payment_method, payment_date, status
    FROM payments
    ORDER BY payment_id
    """)

    payments = cursor.fetchall()

    connection.close()

    return payments


def save_discount(
    discount_id,
    discount_name,
    percentage,
    start_date,
    end_date,
    status
):
    connection = None

    try:
        connection = sqlite3.connect("shophub.db")
        cursor = connection.cursor()

        cursor.execute("""
        INSERT INTO discounts (
            discount_id,
            discount_name,
            percentage,
            start_date,
            end_date,
            status
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """, (
            discount_id,
            discount_name,
            percentage,
            start_date,
            end_date,
            status
        ))

        connection.commit()

        return True

    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False

    finally:
        if connection is not None:
            connection.close()



def get_active_discount():

    today = datetime.now().strftime("%Y-%m-%d")

    connection = sqlite3.connect("shophub.db")
    cursor = connection.cursor()

    cursor.execute("""
    SELECT discount_id,
           discount_name,
           percentage,
           start_date,
           end_date,
           status
    FROM discounts
    WHERE status = 'Active'
      AND start_date <= ?
      AND end_date >= ?
    ORDER BY percentage DESC
    LIMIT 1
    """, (today, today))

    result = cursor.fetchone()

    connection.close()

    return result



def get_all_discounts():

    connection = sqlite3.connect("shophub.db")
    cursor = connection.cursor()

    cursor.execute("""
    SELECT discount_id,
           discount_name,
           percentage,
           start_date,
           end_date,
           status
    FROM discounts
    ORDER BY discount_id
    """)

    discounts = cursor.fetchall()

    connection.close()

    return discounts



def get_total_sales():

    connection = sqlite3.connect("shophub.db")
    cursor = connection.cursor()

    cursor.execute("""
    SELECT COUNT(*)
    FROM orders
    WHERE status = 'Paid'
    """)

    result = cursor.fetchone()

    connection.close()

    return result[0]



def get_total_revenue():

    connection = sqlite3.connect("shophub.db")
    cursor = connection.cursor()

    cursor.execute("""
    SELECT COALESCE(SUM(final_amount), 0)
    FROM orders
    WHERE status = 'Paid'
    """)

    result = cursor.fetchone()

    connection.close()

    return result[0]



def get_best_selling_products():

    connection = sqlite3.connect("shophub.db")
    cursor = connection.cursor()

    cursor.execute("""
    SELECT
        products.product_id,
        products.name,
        SUM(order_items.quantity) AS total_sold
    FROM order_items
    JOIN products
        ON order_items.product_id = products.product_id
    JOIN orders
        ON order_items.order_id = orders.order_id
    WHERE orders.status = 'Paid'
    GROUP BY products.product_id, products.name
    ORDER BY total_sold DESC
    """)

    products = cursor.fetchall()

    connection.close()

    return products



def get_low_stock_products():

    connection = sqlite3.connect("shophub.db")
    cursor = connection.cursor()

    cursor.execute("""
    SELECT product_id, name, category, quantity, product_status
    FROM products
    WHERE quantity <= 5
    ORDER BY quantity ASC
    """)

    products = cursor.fetchall()

    connection.close()

    return products


def get_most_valuable_customers():

    connection = sqlite3.connect("shophub.db")
    cursor = connection.cursor()

    cursor.execute("""
    SELECT
        customers.customer_id,
        customers.full_name,
        customers.email,
        SUM(orders.final_amount) AS total_spent
    FROM customers
    JOIN orders
        ON customers.customer_id = orders.customer_id
    WHERE orders.status = 'Paid'
    GROUP BY customers.customer_id, customers.full_name, customers.email
    ORDER BY total_spent DESC
    """)

    customers = cursor.fetchall()

    connection.close()

    return customers


def get_orders_by_date_range(start_date, end_date):

    connection = sqlite3.connect("shophub.db")
    cursor = connection.cursor()

    cursor.execute("""
    SELECT
        order_id,
        customer_id,
        subtotal,
        discount,
        final_amount,
        order_date,
        status
    FROM orders
    WHERE order_date BETWEEN ? AND ?
    ORDER BY order_date
    """, (start_date, end_date))

    orders = cursor.fetchall()

    connection.close()

    return orders












