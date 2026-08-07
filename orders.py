import database

class Order:

    def __init__(
        self,
        order_id,
        customer_id,
        product_id,
        quantity,
        order_date
    ):
        self.order_id = order_id
        self.customer_id = customer_id
        self.product_id = product_id
        self.quantity = quantity
        self.order_date = order_date

    def confirm_stock_available(self):
        available_quantity = database.get_product_quantity(self.product_id)

        if self.quantity <= available_quantity:
            return True
        else:
            return False

    def calculate_subtotal(self):
        selling_price = database.get_selling_price(self.product_id)

        subtotal = selling_price * self.quantity

        return subtotal

    def calculate_final_amount(self):
        final_amount = self.calculate_subtotal()

        return final_amount

    
    def generate_receipt(self):
        customer_name = database.get_customer_name(self.customer_id)
        product_name = database.get_product_name(self.product_id)

        print("\n=================================")
        print("        SHOPHUB RECEIPT")
        print("=================================")

        print(f"Order ID      : {self.order_id}")
        print(f"Customer      : {customer_name}")
        print(f"Product       : {product_name}")
        print(f"Quantity      : {self.quantity}")
        print(f"Subtotal      : ₦{self.calculate_subtotal()}")
        print(f"Final Amount  : ₦{self.calculate_final_amount()}")
        print(f"Order Date    : {self.order_date}")

        print("=================================")
        print("Thank you for shopping with us!")