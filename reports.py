import os
import database
from datetime import datetime



os.makedirs("generated_reports", exist_ok=True)


def save_report(filename, content):

    try:
        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as file:
            file.write(content)

        return True

    except OSError:
        print("❌ Could not generate the report file.")
        return False


def total_sales():

    total = database.get_total_sales()

    print("\n========== TOTAL SALES ==========")
    print(f"Total Items Sold: {total}")

    content = (
        "========== TOTAL SALES ==========\n"
        f"Total Items Sold: {total}\n"
    )

    if save_report(
        "generated_reports/total_sales.txt",
        content
    ):
        print("✅ Report generated: total_sales.txt")


def total_revenue():

    total = database.get_total_revenue()

    print("\n========== TOTAL REVENUE ==========")
    print(f"Total Revenue: ₦{total}")

    content = (
        "========== TOTAL REVENUE ==========\n"
        f"Total Revenue: ₦{total}\n"
    )

    if save_report(
        "generated_reports/total_revenue.txt",
        content
    ):
        print("✅ Report generated: total_revenue.txt")



def best_selling_products():

    products = database.get_best_selling_products()

    print("\n========== BEST-SELLING PRODUCTS ==========")

    content = (
        "========== BEST-SELLING PRODUCTS ==========\n\n"
    )

    if not products:

        print("No sales recorded.")
        content += "No sales recorded.\n"

    else:

        for number, product in enumerate(products, start=1):

            product_id = product[0]
            name = product[1]
            total_sold = product[2]

            print(
                f"{number}. {name} | "
                f"Product ID: {product_id} | "
                f"Units Sold: {total_sold}"
            )

            content += (
                f"{number}. {name}\n"
                f"Product ID: {product_id}\n"
                f"Units Sold: {total_sold}\n"
                f"----------------------------\n"
            )

    if save_report(
        "generated_reports/best_selling_products.txt",
        content
    ):
        print("✅ Report generated: best_selling_products.txt")


def low_stock():

    products = database.get_low_stock_products()

    print("\n========== LOW-STOCK PRODUCTS ==========")

    content = (
        "========== LOW-STOCK PRODUCTS ==========\n\n"
    )

    if not products:

        print("No low-stock products.")
        content += "No low-stock products.\n"

    else:

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

            content += (
                f"Product ID : {product_id}\n"
                f"Name       : {name}\n"
                f"Category   : {category}\n"
                f"Stock      : {quantity}\n"
                f"Status     : {status}\n"
                f"----------------------------\n"
            )

    if save_report(
        "generated_reports/low_stock_products.txt",
        content
    ):
        print("✅ Report generated: low_stock_products.txt")




def most_valuable_customers():

    customers = database.get_most_valuable_customers()

    print("\n========== MOST VALUABLE CUSTOMERS ==========")

    content = (
        "========== MOST VALUABLE CUSTOMERS ==========\n\n"
    )

    if not customers:

        print("No customer purchases recorded.")
        content += "No customer purchases recorded.\n"

    else:

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

            content += (
                f"{number}. {full_name}\n"
                f"Customer ID: {customer_id}\n"
                f"Email: {email}\n"
                f"Total Spent: ₦{total_spent}\n"
                f"----------------------------\n"
            )

    if save_report(
        "generated_reports/most_valuable_customers.txt",
        content
    ):
        print("✅ Report generated: most_valuable_customers.txt")



def orders_by_date_range():

    print("\n========== ORDERS BY DATE RANGE ==========")

    start_date = input(
        "Enter start date (YYYY-MM-DD): "
    )

    end_date = input(
        "Enter end date (YYYY-MM-DD): "
    )

    try:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")

    except ValueError:
        print("❌ Invalid date format.")
        print("Please use YYYY-MM-DD.")
        return

    if start > end:
        print("❌ Start date cannot be after end date.")
        return

    orders = database.get_orders_by_date_range(
        start_date,
        end_date
    )

    filename = (
        f"generated_reports/"
        f"orders_{start_date}_to_{end_date}.txt"
    )

    content = (
        "========== ORDERS BY DATE RANGE ==========\n"
        f"From: {start_date}\n"
        f"To: {end_date}\n\n"
    )

    if not orders:

        print("No orders found in this date range.")
        content += "No orders found in this date range.\n"

    else:

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

            content += (
                "----------------------------\n"
                f"Order ID     : {order_id}\n"
                f"Customer ID  : {customer_id}\n"
                f"Subtotal     : ₦{subtotal}\n"
                f"Discount     : ₦{discount}\n"
                f"Final Amount : ₦{final_amount}\n"
                f"Order Date   : {order_date}\n"
                f"Status       : {status}\n"
            )

    if save_report(filename, content):
        print(f"✅ Report generated: {filename}")

