# ShopHub Management System

## 1. Project Title

**ShopHub Management System**

---

## 2. Project Story and Background

ShopHub Management System is a console-based business management application developed using **Python and SQLite**.

The project was built as a Python capstone project to demonstrate practical software engineering concepts including **Object-Oriented Programming, database management, modular programming, CRUD operations, authentication, exception handling, and relational database design**.

ShopHub is designed to help small and medium-sized businesses manage their products, customers, shopping carts, orders, payments, discounts, inventory, and business reports from one centralized system.

---

## 3. Problem Being Solved

Many small businesses still rely on notebooks, spreadsheets, or manual processes to manage their products, customers, and sales.

These methods can lead to:

* Lost or misplaced records.
* Incorrect inventory counts.
* Difficulty tracking customer orders.
* Errors when calculating sales.
* Difficulty monitoring business performance.
* Poor organization of customer and payment information.

ShopHub addresses these problems by providing a centralized application that stores business information in an SQLite database and automates important business operations.

---

## 4. Project Objectives

The main objectives of ShopHub are to:

* Manage products and inventory efficiently.
* Register and authenticate customers.
* Provide secure access to the administrative system.
* Allow customers to create and manage shopping carts.
* Process customer orders.
* Automatically calculate order totals and discounts.
* Record customer payments.
* Automatically update inventory after successful purchases.
* Generate useful business reports.
* Demonstrate relational database management using SQLite.
* Demonstrate Object-Oriented Programming with Python.
* Demonstrate modular application development.
* Implement error handling and input validation.

---

## 5. Features

### Product Management

Administrators can:

* Add products.
* View all products.
* Search products by ID, name, or category.
* Update product information.
* Delete products.
* Increase product stock.
* Reduce product stock.
* Monitor product availability.
* Identify low-stock products.

### Customer Management

Customers can:

* Create an account.
* Provide their personal information during registration.
* Validate their email address.
* Validate their phone number.
* Create a password.
* Log into their account.

Customer information is stored permanently in the SQLite database.

### Authentication

The system provides separate authentication for:

**Customers**

* Customer email and password authentication.

**Administrators**

* Administrator username and password authentication.
* Access to the administrative menu after successful authentication.

### Shopping Cart

Customers can:

* Create a shopping cart.
* Add products to their cart.
* Specify product quantities.
* Update cart quantities.
* Remove products from their cart.
* View cart items.
* Calculate the cart total.

The system checks product availability before adding or updating items in the cart.

### Order Management

The system supports:

* Creating orders from customer carts.
* Generating unique Order IDs.
* Recording customer information.
* Recording order subtotal.
* Applying discounts.
* Calculating the final order amount.
* Saving individual products as order items.
* Tracking order status.
* Viewing order details.
* Viewing all orders.

### Inventory Management

ShopHub automatically manages inventory by:

* Checking available stock before purchases.
* Preventing customers from ordering more than available stock.
* Reducing stock after successful purchases.
* Marking products as **Out of Stock** when quantity reaches zero.
* Marking products as **Available** when stock is available.
* Allowing administrators to manually increase or reduce stock.

### Payment Management

The system records:

* Payment ID.
* Associated Order ID.
* Payment amount.
* Payment method.
* Payment date.
* Payment status.

After a successful payment, the corresponding order is automatically marked as **Paid**.

### Discount Management

Administrators can:

* Create discounts.
* Specify discount percentages.
* Set discount start dates.
* Set discount end dates.
* View existing discounts.
* Track discount status.

The system can identify the currently active discount based on its date range and status.

### Business Reports

ShopHub provides several business reports, including:

* Total sales.
* Total revenue.
* Best-selling products.
* Low-stock products.
* Most valuable customers.
* Orders within a specified date range.

These reports allow administrators to understand business performance using information stored in the database.

### Error Handling

The system implements error handling to prevent common problems from crashing the application.

Examples include:

* Invalid email addresses.
* Invalid phone numbers.
* Invalid passwords.
* Duplicate customer email addresses.
* Duplicate customer phone numbers.
* Invalid product quantities.
* Invalid prices.
* Insufficient product stock.
* Non-existent products.
* Invalid administrator credentials.
* Database errors.

---

## 6. Technologies Used

* **Python 3**
* **SQLite**
* **Git**
* **GitHub**
* **Visual Studio Code**

Python's built-in `sqlite3` module is used to communicate with the SQLite database.

---

## 7. Python Concepts Demonstrated

The project demonstrates practical use of:

* Variables
* Data types
* Conditional statements
* Loops
* Functions
* Modules
* Object-Oriented Programming
* Classes
* Constructors
* Instance methods
* Encapsulation
* CRUD operations
* Exception handling
* Regular expressions
* SQLite database integration
* SQL queries
* Primary keys
* Foreign keys
* Table relationships
* JOIN operations
* Aggregate functions
* Menu-driven programming
* String formatting
* Datetime operations
* Modular programming

---

## 8. Database Structure

ShopHub uses **SQLite** as its relational database.

The database contains the following tables:

### Products

Stores information about products available in the shop.

Fields include:

* `product_id`
* `name`
* `category`
* `price`
* `quantity`
* `date_added`
* `product_status`

### Customers

Stores registered customer information.

Fields include:

* `customer_id`
* `full_name`
* `email`
* `phone_number`
* `address`
* `password`
* `registration_date`

### Orders

Stores information about customer orders.

Fields include:

* `order_id`
* `customer_id`
* `subtotal`
* `discount`
* `final_amount`
* `order_date`
* `status`

### Order Items

Stores the individual products belonging to each order.

Fields include:

* `id`
* `order_id`
* `product_id`
* `quantity`
* `unit_price`
* `subtotal`

This allows one order to contain multiple products.

### Carts

Stores active and completed customer shopping carts.

Fields include:

* `cart_id`
* `customer_id`
* `created_at`
* `status`

### Cart Items

Stores the products currently contained in a shopping cart.

Fields include:

* `id`
* `cart_id`
* `product_id`
* `quantity`

### Payments

Stores payment information associated with orders.

Fields include:

* `payment_id`
* `order_id`
* `amount`
* `payment_method`
* `payment_date`
* `status`

### Discounts

Stores available promotional discounts.

Fields include:

* `discount_id`
* `discount_name`
* `percentage`
* `start_date`
* `end_date`
* `status`

### Admins

Stores administrator authentication information.

Fields include:

* `admin_id`
* `username`
* `password`

---

## 9. Database Relationships

The system uses foreign keys to maintain relationships between related tables.

The major relationships include:

* One customer can have multiple orders.
* One customer can have multiple carts.
* One order can contain multiple order items.
* One product can appear in multiple order items.
* One cart can contain multiple cart items.
* One product can appear in multiple cart items.
* One order can have an associated payment.

This relational structure prevents unnecessary duplication of data and keeps the database organized.

---

## 10. Project Structure

The application is divided into multiple Python modules rather than placing the entire system in one file.

Example structure:

```text
ShopHub-Management-System/
│
├── main.py
├── database.py
├── customer.py
├── customer_auth.py
├── admin.py
├── admin_auth.py
├── product.py
├── reports.py
├── validators.py
└── shophub.db
```

### Main Modules

**`main.py`**

Controls the main application menu and connects customers and administrators to their respective sections.

**`database.py`**

Handles SQLite database creation, data storage, retrieval, updates, deletion, authentication, orders, carts, payments, discounts, inventory, and reporting queries.

**`customer.py`**

Contains customer-related functionality and the customer menu.

**`customer_auth.py`**

Handles customer registration and login.

**`admin.py`**

Contains administrative functionality including product management, inventory management, orders, payments, discounts, and access to reports.

**`admin_auth.py`**

Handles administrator authentication.

**`product.py`**

Contains the Product class used to represent products in the system.

**`reports.py`**

Contains business reporting functionality.

**`validators.py`**

Contains input validation functions such as email, phone number, and password validation.

---

## 11. How to Install and Run the Project

### Clone the Repository

```bash
git clone <repository-url>
```

### Open the Project

Open the project folder using Visual Studio Code.

### Install Python

Make sure Python 3 is installed on your computer.

Check the installation using:

```bash
python --version
```

### Run the Application

From the project directory:

```bash
python main.py
```

The application will initialize the required database tables automatically.

---

## 12. How to Use the System

When the application starts, the main menu provides the following options:

```text
========== SHOPHUB ==========
1. Customer Sign Up
2. Customer Login
3. Admin Login
0. Exit
```

### Customer

A customer can:

1. Create an account.
2. Log into their account.
3. Browse products.
4. Add products to a cart.
5. Manage cart quantities.
6. Remove products from the cart.
7. Place orders.
8. Make payments.
9. View order information.

### Administrator

An administrator can log in using administrator credentials and access the administrative menu.

The administrator can:

1. Add products.
2. View products.
3. Search products.
4. Update products.
5. Delete products.
6. Increase stock.
7. Reduce stock.
8. View orders.
9. View order details.
10. View payments.
11. Add discounts.
12. View discounts.
13. View total sales.
14. View total revenue.
15. View best-selling products.
16. View low-stock products.
17. View most valuable customers.
18. View orders by date range.
19. Logout.

---

## 13. Challenges Encountered

Some of the major challenges encountered during development included:

* Designing relationships between multiple database tables.
* Managing foreign key relationships in SQLite.
* Separating orders from individual order items.
* Managing customer shopping carts.
* Preventing customers from ordering unavailable products.
* Updating inventory after successful purchases.
* Managing payment and order statuses.
* Implementing discount functionality.
* Generating unique IDs for different records.
* Handling duplicate customer information.
* Organizing the application into multiple modules.
* Connecting authentication modules to the appropriate menus.
* Implementing exception handling for database operations and invalid input.

---

## 14. Solutions to the Challenges

The following approaches were implemented:

* SQLite foreign keys were used to maintain relationships between related records.
* Separate `orders` and `order_items` tables were used to support multiple products per order.
* Separate `carts` and `cart_items` tables were used to manage shopping carts.
* Reusable database functions were created for database operations.
* Stock availability is checked before products are added to carts or purchased.
* Inventory is automatically updated after successful purchases.
* Unique identifiers are generated for customers, products, carts, orders, payments, and discounts.
* Input validation is used to prevent invalid customer information and invalid numerical values.
* Exception handling is used to handle database-related errors.
* The project is divided into separate modules to improve organization and maintainability.

---

## 15. Possible Future Improvements

Future versions of ShopHub could include:

* Graphical User Interface (GUI).
* Secure password hashing.
* Role-based administrator permissions.
* PDF receipt generation.
* Barcode scanner integration.
* Sales analytics dashboard.
* Product images.
* Customer purchase history.
* Product reviews and ratings.
* Product filtering and advanced search.
* Email notifications.
* Cloud database support.
* REST API integration.
* Mobile application support.
* Multi-user support.
* Online payment gateway integration.
* Automated database backups.

---

## Author

**Divine**

Python Capstone Project

Built with **Python, SQLite, and Object-Oriented Programming**.
