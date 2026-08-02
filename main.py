from product import Product

def main():
    product1 = Product(
    "P001",
    "LED Bulb",
    "Electronics",
    1800,
    2500,
    40
)

    product1.display_product()

    print("\nRestocking...\n")

    product1.restock_product(20)

    print("\nUpdated Product Details:\n")

    product1.display_product()

if __name__ == "__main__":
    main()