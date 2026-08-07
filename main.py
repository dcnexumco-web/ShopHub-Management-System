import product
import customer
import orders
import database
import reports

def main_menu():
    print("\n╔══════════════════════════════════════════════╗")
    print("║          🛒 SHOPHUB MANAGEMENT SYSTEM        ║")
    print("╠══════════════════════════════════════════════╣")
    print("║  1. 📦 Add Product                          ║")
    print("║  2. 👤 Add Customer                         ║")
    print("║  3. 🛍️  Place Order                         ║")
    print("║  4. 📊 View Reports                        ║")
    print("║  5. 🚪 Exit                                ║")
    print("╚══════════════════════════════════════════════╝")

while True:
    main_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        product_id = input("Enter Product ID: ")
        name = input("Enter Product Name: ")
        category = input("Enter Category: ")
        cost_price = float(input("Enter Cost Price: "))
        selling_price = float(input("Enter Selling Price: "))
        quantity = int(input("Enter Quantity: "))
        date_added = input("Enter Date Added (YYYY-MM-DD): ")

        new_product = product.Product(
            product_id,
            name,
            category,
            cost_price,
            selling_price,
            quantity,
            date_added
        )

        database.save_product(new_product)

        print("\nProduct saved successfully.\n")

        new_product.display_product()


    elif choice == "2":
        customer_id = input("Enter Customer ID: ")
        full_name = input("Enter Full Name: ")
        email = input("Enter Email: ")
        phone_number = input("Enter Phone Number: ")
        address = input("Enter Address: ")
        registration_date = input("Enter Registration Date (YYYY-MM-DD): ")

        new_customer = customer.Customer(
        customer_id,
        full_name,
        email,
        phone_number,
        address,
        registration_date
        )

        database.save_customer(new_customer)

        print("\nCustomer saved successfully.\n")

        new_customer.display_customer()

    elif choice == "3":
        order_id = input("Enter Order ID: ")
        customer_id = input("Enter Customer ID: ")
        product_id = input("Enter Product ID: ")
        quantity = int(input("Enter Quantity: "))
        order_date = input("Enter Order Date (YYYY-MM-DD): ")

        if not database.customer_exists(customer_id):
            print("Customer does not exist.")

        elif not database.product_exists(product_id):
            print("Product does not exist.")

        else:
            new_order = orders.Order(
            order_id,
            customer_id,
            product_id,
            quantity,
            order_date
            )

            if not new_order.confirm_stock_available():
                print("Insufficient stock.")

            else:
                database.save_order(new_order)

                available_quantity = database.get_product_quantity(product_id)
                new_quantity = available_quantity - quantity

                database.update_product_quantity(product_id, new_quantity)

                print("════════════════════════════════════════")
                print("✅ Order placed successfully!")
                print("════════════════════════════════════════")

                new_order.generate_receipt()


    elif choice == "4":
        print("\n========== REPORTS ==========")
        print("1. Total Revenue")
        print("2. Low Stock Products")
        print("3. Best Selling Products")
        print("4. Most Valuable Customers")
        print("5. Back to Main Menu")

        report_choice = input("Choose a report: ")

        if report_choice == "1":
            reports.total_revenue()

        elif report_choice == "2":
            reports.low_stock()

        elif report_choice == "3":
            reports.best_selling_products()

        elif report_choice == "4":
            reports.most_valuable_customers()

        elif report_choice == "5":
            continue

        else:
            print("Invalid report choice.")