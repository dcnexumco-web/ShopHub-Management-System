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


add_product()




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