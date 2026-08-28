import database


class Customer:

    def __init__(
        self,
        customer_id,
        full_name,
        email,
        phone_number,
        address,
        password,
        registration_date
    ):
        self.customer_id = customer_id
        self.full_name = full_name
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.password = password
        self.registration_date = registration_date

    def display_customer(self):
        print("\n===== CUSTOMER ACCOUNT =====")
        print(f"Customer ID : {self.customer_id}")
        print(f"Name        : {self.full_name}")
        print(f"Email       : {self.email}")
        print(f"Phone       : {self.phone_number}")
        print(f"Address     : {self.address}")
        print(f"Registered  : {self.registration_date}")


def view_products():

    print("\n========== AVAILABLE PRODUCTS ==========")

    products = database.get_all_products()

    if not products:
        print("No products available.")
        return

    for number, product in enumerate(products, start=1):

        product_id = product[0]
        name = product[1]
        category = product[2]
        price = product[3]
        quantity = product[4]
        status = product[6]

        if status == "Available":
            print(
                f"{number}. {name} | "
                f"{category} | "
                f"₦{price} | "
                f"Stock: {quantity}"
            )




def add_to_cart(customer_id):

    print("\n========== ADD TO CART ==========")

    products = database.get_all_products()

    if not products:
        print("No products available.")
        return

    for number, product in enumerate(products, start=1):

        product_id = product[0]
        name = product[1]
        category = product[2]
        price = product[3]
        quantity = product[4]
        status = product[6]

        if status == "Available":
            print(
                f"{number}. {name} | "
                f"{category} | "
                f"₦{price} | "
                f"Stock: {quantity}"
            )
    try:
        choice = int(input("\nSelect product number: "))

    except ValueError:
        print("❌ Invalid selection. Please enter a valid product number.")
        return

    if choice < 1 or choice > len(products):
        print("❌ Invalid product selection.")
        return

    selected_product = products[choice - 1]

    product_id = selected_product[0]
    name = selected_product[1]

    try:
        quantity = int(input(f"Enter quantity for {name}: "))
    except ValueError:
        print("❌ Invalid quantity. Please enter a valid number.")
        return

    if quantity <= 0:
        print("❌ Quantity must be greater than zero.")
        return  

    cart_id = database.get_active_cart(customer_id)

    if cart_id is None:
        cart_id = database.create_cart(customer_id)

    result = database.add_to_cart(
        cart_id,
        product_id,
        quantity
    )

    if result == "not_found":
        print("❌ Product not found.")

    elif result == "invalid_quantity":
        print("❌ Quantity must be greater than zero.")

    elif result == "insufficient":
        print("❌ Not enough stock available.")

    elif result == "success":
        print("✅ Product added to cart successfully.")


def view_cart(customer_id):

    print("\n========== YOUR CART ==========")

    cart_id = database.get_active_cart(customer_id)

    if cart_id is None:
        print("Your cart is empty.")
        return

    items = database.get_cart_items(cart_id)

    if not items:
        print("Your cart is empty.")
        return

    for number, item in enumerate(items, start=1):

        product_id = item[0]
        name = item[1]
        price = item[2]
        quantity = item[3]
        subtotal = item[4]

        print("\n----------------------------")
        print(f"{number}. {name}")
        print(f"Product ID : {product_id}")
        print(f"Price      : ₦{price}")
        print(f"Quantity   : {quantity}")
        print(f"Subtotal   : ₦{subtotal}")

    total = database.get_cart_total(cart_id)

    print("\n----------------------------")
    print(f"TOTAL      : ₦{total}")


def update_cart(customer_id):

    print("\n========== UPDATE CART ==========")

    cart_id = database.get_active_cart(customer_id)

    if cart_id is None:
        print("Your cart is empty.")
        return

    items = database.get_cart_items(cart_id)

    if not items:
        print("Your cart is empty.")
        return

    print("\nYour cart:")

    for number, item in enumerate(items, start=1):

        product_id = item[0]
        name = item[1]
        quantity = item[3]

        print(f"{number}. {name} - Quantity: {quantity}")
    try:
        choice = int(input("\nSelect product number to update: "))

    except ValueError:
        print("❌ Invalid selection. Please enter a valid product number.")
        return

    if choice < 1 or choice > len(items):
        print("❌ Invalid product selection.")
        return

    selected_item = items[choice - 1]

    product_id = selected_item[0]
    name = selected_item[1]

    try:
        new_quantity = int(
            input(f"Enter new quantity for {name}: ")
        )
    except ValueError:
        print("❌ Invalid quantity. Please enter a valid number.")
        return

    if new_quantity <= 0:
        print("❌ Quantity must be greater than zero.")
        return

    result = database.update_cart_item(
        cart_id,
        product_id,
        new_quantity
    )

    if result == "invalid_quantity":
        print("❌ Quantity must be greater than zero.")

    elif result == "not_found":
        print("❌ Product not found.")

    elif result == "insufficient":
        print("❌ Not enough stock available.")

    elif result == "success":
        print("✅ Cart updated successfully.")



def remove_from_cart(customer_id):

    print("\n========== REMOVE FROM CART ==========")

    cart_id = database.get_active_cart(customer_id)

    if cart_id is None:
        print("Your cart is empty.")
        return

    items = database.get_cart_items(cart_id)

    if not items:
        print("Your cart is empty.")
        return

    print("\nYour cart:")

    for number, item in enumerate(items, start=1):

        product_id = item[0]
        name = item[1]
        quantity = item[3]

        print(f"{number}. {name} - Quantity: {quantity}")

    try:
        choice = int(input("\nSelect product to remove: "))
    except ValueError:
        print("❌ Invalid selection. Please enter a valid product number.")
        return

    if choice < 1 or choice > len(items):
        print("❌ Invalid product selection.")      
        return

    selected_item = items[choice - 1]

    product_id = selected_item[0]
    name = selected_item[1]

    confirmation = input(
        f"Remove {name} from your cart? (yes/no): "
    )

    if confirmation.lower() != "yes":
        print("Removal cancelled.")
        return

    result = database.remove_from_cart(
        cart_id,
        product_id
    )

    if result == "not_found":
        print("❌ Product is not in your cart.")

    elif result == "success":
        print("✅ Product removed from cart.")




def checkout(customer_id):

    print("\n========== CHECKOUT ==========")

    cart_id = database.get_active_cart(customer_id)

    if cart_id is None:
        print("❌ Your cart is empty.")
        return None

    items = database.get_cart_items(cart_id)

    if not items:
        print("❌ Your cart is empty.")
        return None

    print("\n========== ORDER SUMMARY ==========")

    for item in items:

        product_id = item[0]
        name = item[1]
        price = item[2]
        quantity = item[3]
        subtotal = item[4]

        print(f"\nProduct: {name}")
        print(f"Price: ₦{price}")
        print(f"Quantity: {quantity}")
        print(f"Subtotal: ₦{subtotal}")

    subtotal = database.get_cart_total(cart_id)

    discount = 0

    final_amount = subtotal - discount

    print("\n----------------------------")
    print(f"Subtotal    : ₦{subtotal}")
    print(f"Discount    : ₦{discount}")
    print(f"Final Amount: ₦{final_amount}")

    confirmation = input("\nProceed to payment? (yes/no): ")

    if confirmation.lower() != "yes":
        print("Checkout cancelled.")
        return None

    order_id = database.create_order(
        customer_id,
        subtotal,
        discount,
        final_amount
    )

    database.save_order_items(
        order_id,
        cart_id
    )

    print("\n✅ Order created successfully!")
    print(f"Order ID: {order_id}")

    return order_id


def make_payment(order_id):

    print("\n========== PAYMENT ==========")

    order = database.get_order(order_id)

    if order is None:
        print("❌ Order not found.")
        return False

    customer_id = order[1]
    final_amount = order[4]

    cart_id = database.get_active_cart(customer_id)

    if cart_id is None:
        print("❌ Active cart not found.")
        return False

    print(f"\nAmount to pay: ₦{final_amount}")

    print("\nPayment Methods:")
    print("1. Card")
    print("2. Bank Transfer")
    print("3. Cash")

    choice = input("Select payment method: ")

    if choice == "1":
        payment_method = "Card"

    elif choice == "2":
        payment_method = "Bank Transfer"

    elif choice == "3":
        payment_method = "Cash"

    else:
        print("❌ Invalid payment method.")
        return False

    confirmation = input(
        f"Confirm payment of ₦{final_amount}? (yes/no): "
    )

    if confirmation.lower() != "yes":
        print("Payment cancelled.")
        return False

    cart_items = database.get_cart_items(cart_id)

    for item in cart_items:

        product_id = item[0]
        amount = item[3]

        stock_result = database.reduce_stock(
            product_id,
            amount
        )

        if stock_result == "not_found":
            print("❌ A product in your cart no longer exists.")
            return False

        elif stock_result == "insufficient":
            print("❌ There is no longer enough stock for one or more products.")
            return False

        elif stock_result == "database_error":
            print("❌ A database error occurred while updating stock.")
            return False

    payment_id = database.save_payment(
        order_id,
        final_amount,
        payment_method
    )

    if payment_id is None:
        print("❌ Payment could not be recorded.")
        return False

    database.clear_cart(cart_id)

    print("\n✅ Payment successful!")
    print(f"Payment ID: {payment_id}")

    return True





def generate_receipt(order_id):

    print("\n")
    print("======================================")
    print("             SHOPHUB")
    print("              RECEIPT")
    print("======================================")

    order = database.get_order(order_id)

    if order is None:
        print("❌ Order not found.")
        return

    order_id = order[0]
    customer_id = order[1]
    subtotal = order[2]
    discount = order[3]
    final_amount = order[4]
    order_date = order[5]
    status = order[6]

    payment = database.get_payment(order_id)

    customer_data = database.get_customer(customer_id)

    print(f"Order ID    : {order_id}")
    print(f"Customer    : {customer_data[1]}")
    print(f"Email       : {customer_data[2]}")
    print(f"Date        : {order_date}")
    print("--------------------------------------")

    items = database.get_order_items(order_id)

    for item in items:

        product_name = item[0]
        quantity = item[1]
        unit_price = item[2]
        item_subtotal = item[3]

        print(f"\n{product_name}")
        print(f"  {quantity} x ₦{unit_price}")
        print(f"  Subtotal: ₦{item_subtotal}")

    print("--------------------------------------")
    print(f"Subtotal    : ₦{subtotal}")
    print(f"Discount    : ₦{discount}")
    print(f"TOTAL       : ₦{final_amount}")

    if payment is not None:

        payment_id = payment[0]
        payment_method = payment[2]
        payment_date = payment[3]
        payment_status = payment[4]

        print("--------------------------------------")
        print(f"Payment ID  : {payment_id}")
        print(f"Method      : {payment_method}")
        print(f"Payment Date: {payment_date}")
        print(f"Status      : {payment_status}")

    print("======================================")
    print("        THANK YOU FOR SHOPPING!")
    print("======================================")



def customer_menu(customer_data):

    customer_id = customer_data[0]

    while True:

        print("\n========== CUSTOMER MENU ==========")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Update Cart")
        print("5. Remove from Cart")
        print("6. Checkout")
        print("7. Make Payment")
        print("8. Generate Receipt")
        print("9. View Profile")
        print("0. Logout")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            view_products()

        elif choice == "2":
            add_to_cart(customer_id)

        elif choice == "3":
            view_cart(customer_id)

        elif choice == "4":
            update_cart(customer_id)

        elif choice == "5":
            remove_from_cart(customer_id)

        elif choice == "6":
            checkout(customer_id)

        elif choice == "7":
            order_id = input("Enter Order ID: ")
            make_payment(order_id)

        elif choice == "8":
            order_id = input("Enter Order ID: ")
            generate_receipt(order_id)

        elif choice == "9":
            customer_object = Customer(
                customer_data[0],
                customer_data[1],
                customer_data[2],
                customer_data[3],
                customer_data[4],
                "",
                customer_data[5]
            )

            customer_object.display_customer()

        elif choice == "0":
            print("\nLogging out...")
            break

        else:
            print("❌ Invalid choice. Please try again.")

