import product
import database
import datetime
import reports


def add_product():

    print("\n========== ADD PRODUCT ==========")

    name = input("Enter product name: ")
    category = input("Enter category: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    product_id = database.generate_product_id()
    date_added = database.get_current_date()

    new_product = product.Product(
        product_id,
        name,
        category,
        price,
        quantity,
        date_added
    )

    database.save_product(new_product)

    print("\n✅ Product added successfully!")
    new_product.display_product()







def view_products():

    print("\n========== ALL PRODUCTS ==========")

    products = database.get_all_products()

    if not products:
        print("No products found.")
        return

    for product in products:
        print("\n----------------------------")
        print(f"Product ID : {product[0]}")
        print(f"Name       : {product[1]}")
        print(f"Category   : {product[2]}")
        print(f"Price      : ₦{product[3]}")
        print(f"Quantity   : {product[4]}")
        print(f"Date Added : {product[5]}")
        print(f"Status     : {product[6]}")




def search_products():

    print("\n========== SEARCH PRODUCTS ==========")

    search_term = input("Enter product ID, name, or category: ")

    products = database.search_product(search_term)

    if not products:
        print("❌ No products found.")
        return

    for product in products:
        print("\n----------------------------")
        print(f"Product ID : {product[0]}")
        print(f"Name       : {product[1]}")
        print(f"Category   : {product[2]}")
        print(f"Price      : ₦{product[3]}")
        print(f"Quantity   : {product[4]}")
        print(f"Date Added : {product[5]}")
        print(f"Status     : {product[6]}")


def update_product():

    print("\n========== UPDATE PRODUCT ==========")

    product_id = input("Enter product ID: ")

    products = database.search_product(product_id)

    if not products:
        print("❌ Product not found.")
        return

    print("Leave a field unchanged by entering the current value.")

    name = input("Enter new product name: ")
    category = input("Enter new category: ")
    
    try:
        price = float(input("Enter new price: "))
    except ValueError:
        print("❌ Invalid price. Please enter a valid number.")
        return

    result = database.update_product(
        product_id,
        name,
        category,
        price
    )

    if result > 0:
        print("\n✅ Product updated successfully.")
    else:
        print("\n❌ Product could not be updated.")



def delete_product():

    print("\n========== DELETE PRODUCT ==========")

    product_id = input("Enter product ID: ")

    products = database.search_product(product_id)

    if not products:
        print("❌ Product not found.")
        return

    print(f"Product: {products[0][1]}")

    confirmation = input("Are you sure you want to delete this product? (yes/no): ")

    if confirmation.lower() != "yes":
        print("Deletion cancelled.")
        return

    result = database.delete_product(product_id)

    if result > 0:
        print("\n✅ Product deleted successfully.")
    else:
        print("\n❌ Product could not be deleted.")



def increase_product_stock():

    print("\n========== INCREASE STOCK ==========")

    product_id = input("Enter product ID: ")
    try:
        amount = int(input("Enter quantity to add: "))
    except ValueError:
        print("❌ Invalid quantity. Please enter a valid number.")
        return

    if amount <= 0:
        print("❌ Quantity must be greater than zero.")
        return

    result = database.increase_stock(
        product_id,
        amount
    )

    if result > 0:
        print("\n✅ Stock increased successfully.")
    else:
        print("\n❌ Product not found.")


def reduce_product_stock():

    print("\n========== REDUCE STOCK ==========")

    product_id = input("Enter product ID: ")
    try:
        amount = int(input("Enter quantity to remove: "))
    except ValueError:
        print("❌ Invalid quantity. Please enter a valid number.")
        return

    if amount <= 0:
        print("❌ Quantity must be greater than zero.")
        return

    result = database.reduce_stock(
        product_id,
        amount
    )

    if result == "not_found":
        print("❌ Product not found.")

    elif result == "insufficient":
        print("❌ Cannot reduce stock below zero.")

    elif result == "success":
        print("✅ Stock reduced successfully.")


def view_orders():

    print("\n========== ALL ORDERS ==========")

    orders = database.get_all_orders()

    if not orders:
        print("No orders found.")
        return

    for order in orders:

        order_id = order[0]
        customer_id = order[1]
        subtotal = order[2]
        discount = order[3]
        final_amount = order[4]
        order_date = order[5]
        status = order[6]

        print("\n----------------------------")
        print(f"Order ID    : {order_id}")
        print(f"Customer ID : {customer_id}")
        print(f"Subtotal    : ₦{subtotal}")
        print(f"Discount    : ₦{discount}")
        print(f"Final Amount: ₦{final_amount}")
        print(f"Order Date  : {order_date}")
        print(f"Status      : {status}")



def view_order_details():

    print("\n========== ORDER DETAILS ==========")

    order_id = input("Enter order ID: ")

    order = database.get_order(order_id)

    if order is None:
        print("❌ Order not found.")
        return

    print(f"\nOrder ID    : {order[0]}")
    print(f"Customer ID : {order[1]}")
    print(f"Subtotal    : ₦{order[2]}")
    print(f"Discount    : ₦{order[3]}")
    print(f"Final Amount: ₦{order[4]}")
    print(f"Order Date  : {order[5]}")
    print(f"Status      : {order[6]}")

    items = database.get_order_items(order_id)

    print("\n========== ORDER ITEMS ==========")

    for item in items:

        product_name = item[0]
        quantity = item[1]
        unit_price = item[2]
        subtotal = item[3]

        print("\n----------------------------")
        print(f"Product  : {product_name}")
        print(f"Quantity : {quantity}")
        print(f"Unit Price: ₦{unit_price}")
        print(f"Subtotal : ₦{subtotal}")



def view_payments():

    print("\n========== ALL PAYMENTS ==========")

    payments = database.get_all_payments()

    if not payments:
        print("No payments found.")
        return

    for payment in payments:

        payment_id = payment[0]
        order_id = payment[1]
        amount = payment[2]
        payment_method = payment[3]
        payment_date = payment[4]
        status = payment[5]

        print("\n----------------------------")
        print(f"Payment ID : {payment_id}")
        print(f"Order ID   : {order_id}")
        print(f"Amount     : ₦{amount}")
        print(f"Method     : {payment_method}")
        print(f"Date       : {payment_date}")
        print(f"Status     : {status}")



def add_discount():

    print("\n========== ADD DISCOUNT ==========")

    discount_name = input("Enter discount name: ")

    try:
        percentage = float(
            input("Enter discount percentage: ")
        )
    except ValueError:
        print("❌ Invalid percentage. Please enter a valid number.")
        return

    if percentage <= 0 or percentage > 100:
        print("❌ Percentage must be between 1 and 100.")
        return

    try:
        duration = int(
            input("Enter discount duration (days): ")
        )
    except ValueError:
        print("❌ Invalid duration. Please enter a valid number.")
        return

    if duration <= 0:
        print("❌ Duration must be greater than zero.")
        return

    start_date = datetime.now()

    end_date = start_date + timedelta(days=duration)

    start_date = start_date.strftime("%Y-%m-%d")
    end_date = end_date.strftime("%Y-%m-%d")

    discount_id = database.generate_discount_id()

    status = "Active"

    database.save_discount(
        discount_id,
        discount_name,
        percentage,
        start_date,
        end_date,
        status
    )

    print("\n✅ Discount created successfully!")
    print(f"Discount ID : {discount_id}")
    print(f"Name        : {discount_name}")
    print(f"Percentage  : {percentage}%")
    print(f"Start Date  : {start_date}")
    print(f"End Date    : {end_date}")
    print(f"Status      : {status}")



def view_discounts():

    print("\n========== ALL DISCOUNTS ==========")

    discounts = database.get_all_discounts()

    if not discounts:
        print("No discounts found.")
        return

    for discount in discounts:

        print("\n----------------------------")
        print(f"Discount ID : {discount[0]}")
        print(f"Name        : {discount[1]}")
        print(f"Percentage  : {discount[2]}%")
        print(f"Start Date  : {discount[3]}")
        print(f"End Date    : {discount[4]}")
        print(f"Status      : {discount[5]}")




def view_total_sales():

    print("\n========== TOTAL SALES ==========")

    total_sales = database.get_total_sales()

    print(f"Total Sales: {total_sales}")



def view_total_revenue():

    print("\n========== TOTAL REVENUE ==========")

    total_revenue = database.get_total_revenue()

    print(f"Total Revenue: ₦{total_revenue}")



def view_best_selling_products():

    print("\n========== BEST-SELLING PRODUCTS ==========")

    products = database.get_best_selling_products()

    if not products:
        print("No sales recorded yet.")
        return

    for number, product in enumerate(products, start=1):

        product_id = product[0]
        name = product[1]
        total_sold = product[2]

        print(
            f"{number}. {name} | "
            f"Product ID: {product_id} | "
            f"Units Sold: {total_sold}"
        )



def view_low_stock_products():

    print("\n========== LOW-STOCK PRODUCTS ==========")

    products = database.get_low_stock_products()

    if not products:
        print("No low-stock products.")
        return

    for product in products:

        product_id = product[0]
        name = product[1]
        category = product[2]
        quantity = product[3]
        status = product[4]

        print("\n----------------------------")
        print(f"Product ID : {product_id}")
        print(f"Name       : {name}")
        print(f"Category   : {category}")
        print(f"Stock      : {quantity}")
        print(f"Status     : {status}")




def view_most_valuable_customers():

    print("\n========== MOST VALUABLE CUSTOMERS ==========")

    customers = database.get_most_valuable_customers()

    if not customers:
        print("No customer purchases recorded yet.")
        return

    for number, customer in enumerate(customers, start=1):

        customer_id = customer[0]
        full_name = customer[1]
        email = customer[2]
        total_spent = customer[3]

        print(
            f"{number}. {full_name} | "
            f"Customer ID: {customer_id} | "
            f"Total Spent: ₦{total_spent}"
        )




def view_orders_by_date_range():

    print("\n========== ORDERS BY DATE RANGE ==========")

    try:
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")
    except ValueError:
        print("❌ Invalid date format. Please enter dates in YYYY-MM-DD format.")
        return

    orders = database.get_orders_by_date_range(
        start_date,
        end_date
    )

    if not orders:
        print("No orders found in this date range.")
        return

    for order in orders:

        order_id = order[0]
        customer_id = order[1]
        subtotal = order[2]
        discount = order[3]
        final_amount = order[4]
        order_date = order[5]
        status = order[6]

        print("\n----------------------------")
        print(f"Order ID     : {order_id}")
        print(f"Customer ID  : {customer_id}")
        print(f"Subtotal     : ₦{subtotal}")
        print(f"Discount     : ₦{discount}")
        print(f"Final Amount : ₦{final_amount}")
        print(f"Order Date   : {order_date}")
        print(f"Status       : {status}")






def admin_menu():

    while True:

        print("\n========== ADMIN MENU ==========")
        print("1. Add Product")
        print("2. View Products")
        print("3. Search Products")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Increase Stock")
        print("7. Reduce Stock")
        print("8. View Orders")
        print("9. View Order Details")
        print("10. View Payments")
        print("11. Add Discount")
        print("12. View Discounts")
        print("13. Total Sales")
        print("14. Total Revenue")
        print("15. Best-Selling Products")
        print("16. Low-Stock Products")
        print("17. Most Valuable Customers")
        print("18. Orders by Date Range")
        print("19. Logout")

        choice = input("\nSelect an option: ")

        if choice == "1":
            add_product()

        elif choice == "2":
            view_products()

        elif choice == "3":
            search_products()

        elif choice == "4":
            update_product()

        elif choice == "5":
            delete_product()

        elif choice == "6":
            increase_product_stock()

        elif choice == "7":
            reduce_product_stock()

        elif choice == "8":
            view_orders()

        elif choice == "9":
            view_order_details()

        elif choice == "10":
            view_payments()

        elif choice == "11":
            add_discount()

        elif choice == "12":
            view_discounts()

        elif choice == "13":
            reports.total_sales()

        elif choice == "14":
            reports.total_revenue()

        elif choice == "15":
            reports.best_selling_products()

        elif choice == "16":
            reports.low_stock()

        elif choice == "17":
            reports.most_valuable_customers()

        elif choice == "18":
            reports.orders_by_date_range()

        elif choice == "19":
            print("\nLogging out...")
            break

        else:
            print("❌ Invalid option.")