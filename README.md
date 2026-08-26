# ShopHub Management System

## 1. Project Title

**ShopHub Management System**

---

## 2. Project Story and Background

ShopHub Management System is a console-based business management application developed using **Python and SQLite**.

The project was built as a Python capstone project to demonstrate practical software engineering concepts including **Object-Oriented Programming, database management, modular programming, CRUD operations, authentication, exception handling, input validation, and relational database design**.

ShopHub is designed to help small and medium-sized businesses manage products, customers, shopping carts, orders, payments, discounts, inventory, and business reports from one centralized system.

---

## 3. Problem Being Solved

Small retail businesses need to keep track of products, customer purchases, inventory, payments, and sales. When these activities are handled manually or through separate records, it can become difficult to keep information organized and maintain accurate stock levels.

For example, a shop may need to know:

* Which products are currently available.
* How many units of each product are in stock.
* What products a customer has ordered.
* How much a customer needs to pay.
* Whether an order has been paid for.
* Which products are selling the most.
* How much revenue the shop has generated.
* Which products are running low on stock.

ShopHub addresses this problem by providing a centralized console-based shopping and store management system. Customers can create accounts, browse products, manage their carts, place orders, and make payments, while administrators can manage products, inventory, orders, payments, discounts, and sales reports.

The system also connects these activities through a relational SQLite database, allowing information such as customers, products, carts, orders, and payments to be stored and related in an organized way.


## 4. Project Objectives

The main objectives of ShopHub are to:

* Manage products and inventory efficiently.
* Register and authenticate customers.
* Provide administrator authentication.
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
* Provide their information during registration.
* Validate their email address.
* Validate their phone number.
* Create a password.
* Log into their account.

Customer information is stored in the SQLite database.

### Authentication

ShopHub uses a **single login entry point** for both customers and administrators.

Users provide a username/email and password.

The system checks the credentials against the database:

* Administrator username and password → Administrator menu.
* Customer email and password → Customer menu.
* Invalid credentials → Login is rejected.

This avoids exposing a separate administrator login option on the main menu.

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
* Recording the customer associated with an order.
* Recording order subtotal.
* Applying discounts.
* Calculating the final order amount.
* Saving individual products as order items.
* Tracking order status.
* Viewing order details.
* Viewing all orders.

### Inventory Management

ShopHub manages inventory by:

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

The system identifies an active discount based on its status and date range.

### Business Reports

ShopHub provides reports including:

* Total sales.
* Total revenue.
* Best-selling products.
* Low-stock products.
* Most valuable customers.
* Orders within a specified date range.

These reports help administrators monitor business performance using information stored in the database.

### Error Handling and Input Validation

The system handles common errors such as:

* Invalid email addresses.
* Invalid phone numbers.
* Invalid passwords.
* Duplicate customer email addresses.
* Duplicate customer phone numbers.
* Invalid product quantities.
* Invalid prices.
* Insufficient product stock.
* Non-existent products.
* Invalid login credentials.
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

Stores customer shopping carts.

Fields include:

* `cart_id`
* `customer_id`
* `created_at`
* `status`

### Cart Items

Stores the products contained in a shopping cart.

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

Stores promotional discounts.

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
* An order can have an associated payment.

This relational structure reduces unnecessary duplication and keeps related business information organized.

---

## 10. Project Structure

The application is divided into multiple Python modules rather than placing the entire system in one file.

```text
ShopHub-Management-System/
│
├── main.py
├── database.py
├── customer.py
├── customer_auth.py
├── admin.py
├── product.py
├── reports.py
├── validators.py
├── .gitignore
└── shophub.db
```

> `shophub.db` is a local SQLite database file and is excluded from Git tracking using `.gitignore`.

### Main Modules

**`main.py`**

Controls the main application menu and provides the single login entry point for customers and administrators.

**`database.py`**

Handles SQLite database creation, data storage, retrieval, updates, deletion, authentication, orders, carts, payments, discounts, inventory, and reporting queries.

**`customer.py`**

Contains customer-related functionality and the customer menu.

**`customer_auth.py`**

Handles customer registration and customer authentication.

**`admin.py`**

Contains administrative functionality including product management, inventory management, orders, payments, discounts, and access to reports.

**`product.py`**

Contains the `Product` class used to represent products in the system.

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

Make sure Python 3 is installed.

Check the installation using:

```bash
python --version
```

### Run the Application

From the project directory:

```bash
python main.py
```

The application automatically creates the required database tables and default administrator account if they do not already exist.

---

## 12. How to Use the System

When the application starts, the main menu provides three options:

```text
========== SHOPHUB ==========
1. Login
2. Sign Up
0. Exit
```

### Login

Both customers and administrators use the same login option.

```text
========== LOGIN ==========
Enter username/email:
Enter password:
```

The system determines the account type from the credentials provided.

A valid administrator account is sent to the administrator menu, while a valid customer account is sent to the customer menu.

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

An administrator can:

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
* Connecting authentication to the appropriate user menus.
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
* Input validation is used to prevent invalid customer information and numerical values.
* Exception handling is used to handle database-related errors.
* The application uses a single login entry point for both customers and administrators.
* The project is divided into separate modules to improve organization and maintainability.

---

## 15. Possible Future Improvements

Future versions of ShopHub could include:

* Secure password hashing.
* Role-based administrator permissions.
* Graphical User Interface (GUI).
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

**Divine Chukwudi**

Python Capstone Project

Built with **Python, SQLite, and Object-Oriented Programming**.
