# Inventory Management System

## Overview

The Inventory Management System is a Flask-based REST API and Command Line Interface (CLI) application for managing product inventory. It allows users to add, view, update, delete, and search products while integrating with the OpenFoodFacts API to automatically retrieve product information using a barcode or product name.

The project demonstrates object-oriented programming (OOP), RESTful API development, external API integration, and unit testing in Python.

---

## Features

* View all inventory items
* View a single product by ID
* Add new products using a barcode
* Automatically fetch product information from OpenFoodFacts
* Update product price and stock
* Delete products from inventory
* Search products by barcode
* Search products by name
* Command Line Interface (CLI)
* Unit tests for core business logic

---

## Technologies Used

* Python 3
* Flask
* Requests
* Pytest
* OpenFoodFacts API

---

## Project Structure

```text
Inventory_Flask.py/
│
├── app.py
├── requirements.txt
├── README.md
│
├── cli/
│   └── cli.py
│
├── data/
│   └── inventory.py
│
├── models/
│   ├── inventory_item.py
│   └── inventory_manager.py
│
├── routes/
│   └── inventory_routes.py
│
├── services/
│   └── openfoodfacts.py
│
├── tests/
│   └── unit/
│       └── test_inventory_manager.py
│
└── utils/
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/tripplek2/Inventory_system_Flask.py.git
cd Inventory_Flask.py
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
```

### 3. Activate the virtual environment

Linux/macOS

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Flask API

Start the Flask development server:

```bash
python3 app.py
```

The server runs at:

```text
http://127.0.0.1:5000
```

---

## Running the CLI

Open another terminal, activate the virtual environment, then run:

```bash
python3 cli/cli.py
```

The CLI menu provides options to:

* View Inventory
* View Product
* Add Product
* Update Product
* Delete Product
* Search Product by Barcode
* Search Product by Name

---

## API Endpoints

| Method | Endpoint                      | Description                          |
| ------ | ----------------------------- | ------------------------------------ |
| GET    | `/inventory`                  | Get all inventory items              |
| GET    | `/inventory/<item_id>`             | Get a product by ID                  |
| POST   | `/inventory`                  | Add a new product                    |
| PATCH  | `/inventory/<item_id>`             | Update a product                     |
| DELETE | `/inventory/<item_id>`             | Delete a product                     |
| GET    | `/openfood/barcode/<barcode>` | Search OpenFoodFacts by barcode      |
| GET    | `/openfood/name/<name>`       | Search OpenFoodFacts by product name |

---

## Running Tests

Run all tests:
* pytest -v

Run only the Inventory Manager tests:
* pytest tests/unit/test_inventory_manager.py -v


## Future Improvements

* Replace the in-memory inventory with a SQL database.
* Add user authentication.
* Add product categories and reports.
* Deploy the application to a cloud platform.

---

## Author

**Kelvin Korir** 
