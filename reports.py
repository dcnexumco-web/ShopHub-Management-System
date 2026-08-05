import database

def total_sales():
    total = database.get_total_sales()

    print(f"Total Items Sold: {total}")