class Customer:
    def __init__(
        self,
        customer_id,
        full_name,
        email,
        phone_number,
        address,
        registration_date
    ):
        self.customer_id = customer_id
        self.full_name = full_name
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.registration_date = registration_date

    def display_customer(self):
        print("\n===== CUSTOMER DETAILS =====")
        print(f"Customer ID : {self.customer_id}")
        print(f"Name        : {self.full_name}")
        print(f"Email       : {self.email}")
        print(f"Phone       : {self.phone_number}")
        print(f"Address     : {self.address}")
        print(f"Registration Date : {self.registration_date}")