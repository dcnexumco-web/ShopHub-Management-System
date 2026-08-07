# ShopHub Management System

## 1. Project Title

**ShopHub Management System**

---

## 2. Project Story and Background

ShopHub Management System is a console-based business management application developed using Python and SQLite. The project was built as a capstone project to demonstrate software engineering principles, object-oriented programming, database management, and modular application development.

The system is designed to help small and medium-sized businesses efficiently manage products, customers, orders, inventory, and business reports. Rather than relying on paper records or spreadsheets, ShopHub provides a centralized system for storing and managing business information.

---

## 3. Problem Being Solved

Many small businesses still record customer information, product inventory, and sales manually. These methods often result in:

* Lost or misplaced records.
* Incorrect inventory counts.
* Slow order processing.
* Difficulty calculating sales.
* Inaccurate business reports.

ShopHub solves these problems by storing business information electronically using an SQLite database while automating inventory updates, sales calculations, and report generation.

---

## 4. Project Objectives

The objectives of this project are to:

* Manage products efficiently.
* Register and manage customers.
* Process customer orders.
* Automatically update inventory after every sale.
* Generate useful business reports.
* Demonstrate Object-Oriented Programming using Python.
* Demonstrate database management using SQLite.
* Build a menu-driven application using modular programming.

---

## 5. Features

The ShopHub Management System includes the following features:

### Product Management

* Add new products.
* Store product information permanently.
* Track available stock.
* Update inventory automatically after sales.

### Customer Management

* Register customers.
* Validate email addresses.
* Validate phone numbers using Regular Expressions.
* Store customer information permanently.

### Order Management

* Place customer orders.
* Verify customer existence using phone number lookup.
* Verify product availability before completing an order.
* Automatically calculate:

  * Subtotal
  * Final Amount
* Automatically reduce product quantity after successful purchases.
* Generate professional sales receipts.

### Reports

* Total Revenue Report
* Low Stock Products Report
* Best Selling Products Report
* Most Valuable Customers Report

### Error Handling

* Prevent duplicate Order IDs.
* Prevent invalid customer records.
* Prevent ordering unavailable products.
* Handle database errors gracefully without crashing.

---

## 6. Technologies Used

* Python 3
* SQLite
* Git
* GitHub
* Visual Studio Code

---

## 7. Python Concepts Demonstrated

This project demonstrates the practical application of several Python concepts, including:

* Variables
* Data Types
* Conditional Statements
* Loops
* Functions
* Modules
* Object-Oriented Programming (Classes, Constructors, Instance Methods)
* File Organization
* Exception Handling
* Regular Expressions
* SQLite Database Integration
* CRUD Operations
* SQL Queries
* Menu-Driven Programming
* Datetime Module

---

## 8. Database Structure

The project uses SQLite for permanent data storage.

### Products Table

* Product ID
* Product Name
* Category
* Cost Price
* Selling Price
* Quantity
* Date Added

### Customers Table

* Customer ID
* Full Name
* Email
* Phone Number
* Address
* Registration Date

### Orders Table

* Order ID
* Customer ID
* Product ID
* Quantity
* Subtotal
* Final Amount
* Order Date

Relationships are maintained using foreign keys between customers, products, and orders.

---

## 9. How to Install and Run the Project

### Clone the repository

```bash
git clone <repository-url>
```

### Open the project

Open the project folder using Visual Studio Code.

### Install Python

Ensure Python 3 is installed on your computer.

### Run the application

```bash
python main.py
```

The SQLite database (`shophub.db`) will be created automatically if it does not already exist.

---

## 10. How to Use the System

When the application starts, the main menu is displayed.

Users can:

1. Add Products
2. Register Customers
3. Place Orders
4. View Business Reports
5. Exit the application

The system automatically validates input, stores information in the database, updates inventory, and generates receipts after successful orders.

---

## 11. Challenges Encountered

Some of the major challenges encountered during development included:

* Designing relationships between products, customers, and orders.
* Managing foreign key relationships in SQLite.
* Updating inventory automatically after every completed order.
* Looking up customers using phone numbers while storing Customer IDs internally.
* Preventing duplicate Order IDs.
* Creating readable sales receipts.
* Organizing the project into multiple Python modules instead of one large file.

---

## 12. Solutions to the Challenges

The following solutions were implemented:

* Used SQLite foreign keys to maintain data relationships.
* Created reusable database functions for querying records.
* Implemented inventory updates immediately after successful purchases.
* Used phone number lookup to retrieve Customer IDs automatically.
* Added exception handling using `try`, `except`, and `finally` to prevent application crashes.
* Improved receipt formatting for better readability.
* Divided the project into separate modules for maintainability and readability.

---

## 13. Possible Future Improvements

Future versions of ShopHub may include:

* Graphical User Interface (GUI)
* User Authentication and Authorization
* Barcode Scanner Integration
* PDF Receipt Generation
* Sales Analytics Dashboard
* Cloud Database Support
* Automatic Order ID Generation
* Customer Purchase History
* Product Search and Filtering
* Multi-user Support
* REST API Integration
* Mobile Application Support

---

## Author

**Divine**

Python Capstone Project

Built with Python, SQLite, and Object-Oriented Programming.
