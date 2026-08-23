class Product:

    def __init__(
        self,
        product_id,
        name,
        category,
        price,
        quantity,
        date_added
    ):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity
        self.date_added = date_added

        if self.quantity > 0:
            self.product_status = "Available"
        else:
            self.product_status = "Out of Stock"

    def display_product(self):
        print("\n===== PRODUCT DETAILS =====")
        print(f"Product ID      : {self.product_id}")
        print(f"Name            : {self.name}")
        print(f"Category        : {self.category}")
        print(f"Price           : ₦{self.price}")
        print(f"Quantity        : {self.quantity}")
        print(f"Date Added      : {self.date_added}")
        print(f"Status          : {self.product_status}")

    def restock_product(self, amount):

        if amount <= 0:
            print("Restock quantity must be greater than zero.")
            return

        self.quantity += amount
        self.product_status = "Available"

        print(f"{amount} items added successfully.")
        print(f"New stock: {self.quantity}")

    def sell_product(self, amount):

        if amount <= 0:
            print("Sell quantity must be greater than zero.")
            return

        if amount > self.quantity:
            print("Insufficient stock to sell.")
            return

        self.quantity -= amount

        if self.quantity == 0:
            self.product_status = "Out of Stock"

        print(f"{amount} items sold successfully.")
        print(f"Remaining stock: {self.quantity}")