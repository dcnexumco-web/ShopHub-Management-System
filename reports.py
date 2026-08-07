import database

def total_sales():
    total = database.get_total_sales()

    print(f"Total Items Sold: {total}")

def total_revenue():
    total = database.get_total_revenue()

    print(f"Total Revenue: ₦{total}")


def low_stock():
    low_stock_products = database.get_low_stock()

    if not low_stock_products:
        print("No low stock products.")
    else:
        print("Low Stock Products:")
        for product in low_stock_products:
            print(f" - {product[1]}: {product[5]} units")

def most_valuable_customers():
    valuable_customers = database.get_most_valuable_customers()

    if not valuable_customers:
        print("No customers found.")
    else:
        print("Most Valuable Customers:")
        for customer in valuable_customers:
            print(f" - {customer[0]}: ₦{customer[1]} total spent")


def best_selling_products():
    products = database.get_best_selling_products()

    if not products:
        print("No products found.")
    else:
        print("\n===== BEST SELLING PRODUCTS =====")

        for product in products:
            print(f"Product ID: {product[0]}")
            print(f"Quantity Sold: {product[1]}")
            print("----------------------------")