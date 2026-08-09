import database

def total_sales():
    total = database.get_total_sales()

    print(f"Total Items Sold: {total}")

    with open("generated_reports/total_sales.txt", "w", encoding="utf-8") as file:
        file.write(f"Total Items Sold: {total}")

def total_revenue():
    total = database.get_total_revenue()

    print(f"Total Revenue: ₦{total}")

    with open("generated_reports/total_revenue.txt", "w", encoding="utf-8") as file:
        file.write(f"Total Revenue: ₦{total}")

def low_stock():
    low_stock_products = database.get_low_stock()

    if not low_stock_products:
        print("No low stock products.")
    else:
        print("Low Stock Products:")
        for product in low_stock_products:
            print(f" - {product[1]}: {product[5]} units")

    with open("generated_reports/low_stock.txt", "w", encoding="utf-8") as file:
        if not low_stock_products:
            file.write("No low stock products.")
        else:
            file.write("Low Stock Products:\n")
            for product in low_stock_products:
                file.write(f" - {product[1]}: {product[5]} units\n")

def most_valuable_customers():
    valuable_customers = database.get_most_valuable_customers()

    if not valuable_customers:
        print("No customers found.")
    else:
        print("Most Valuable Customers:")
        for customer in valuable_customers:
            print(f" - {customer[0]}: ₦{customer[1]} total spent")

    with open("generated_reports/most_valuable_customers.txt", "w", encoding="utf-8") as file:
        if not valuable_customers:
            file.write("No customers found.")
        else:
            file.write("Most Valuable Customers:\n")
            for customer in valuable_customers:
                file.write(f" - {customer[0]}: ₦{customer[1]} total spent\n")


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

    with open("generated_reports/best_selling_products.txt", "w", encoding="utf-8") as file:
        if not products:
            file.write("No products found.")
        else:
            file.write("===== BEST SELLING PRODUCTS =====\n")
            for product in products:
                file.write(f"Product ID: {product[0]}\n")
                file.write(f"Quantity Sold: {product[1]}\n")
                file.write("----------------------------\n")