import product
import database


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
    price = float(input("Enter new price: "))

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
    amount = int(input("Enter quantity to add: "))

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
    amount = int(input("Enter quantity to remove: "))

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