class Product:
    def __init__(self, product_id, name, category, cost_price, selling_price, quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.cost_price = cost_price
        self.selling_price = selling_price
        self.quantity = quantity


    
    def display_product(self):
        print("\n===== PRODUCT DETAILS =====")
        print(f"Product ID : {self.product_id}")
        print(f"Name       : {self.name}")
        print(f"Category   : {self.category}")
        print(f"Cost Price : ₦{self.cost_price}")
        print(f"Selling Price : ₦{self.selling_price}")
        print(f"Quantity   : {self.quantity}")



    def restock_product(self, amount):
        if amount <= 0:
            print("Restock quantity must be greater than zero.")
            return

        self.quantity += amount
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
        print(f"{amount} items sold successfully.")
        print(f"Remaining stock: {self.quantity}") 