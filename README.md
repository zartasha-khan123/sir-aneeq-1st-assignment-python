 Inventory Management System – Documentation
🧾 Overview
This project is a dual-interface Inventory Management System that allows users to manage electronic products. It supports both:

A Command-Line Interface (CLI) for terminal usage.

A Streamlit-based Web UI for a graphical, browser-based experience.

The system enables users to add products, list them, and view total inventory value.

🗂️ Project Structure
lua
Copy
Edit
main.py  <-- Single Python file for both CLI & Web UI
🔧 Features
✅ Core Functionalities
Add electronic products with details like name, price, quantity, brand, and warranty.

View a list of all available products.

Calculate and display total inventory value.

✅ Product Types
Supports generic products via the Product class.

Supports electronic products with extended details via Electronics class.

🧠 Classes Description
Product
Represents a basic product.

Attribute	Description
pid	Product ID
name	Product name
price	Unit price (float)
quantity	Stock quantity (int)

Methods:

total_value(): Returns price × quantity

__str__(): Nicely formatted product string

Electronics(Product)
Extends Product with:

Attribute	Description
warranty_years	Warranty in yrs
brand	Brand name

Inventory
Manages a collection of products.

Methods:

add_product(product): Adds or updates quantity if product exists

list_all_products(): Returns a list of all products

total_inventory_value(): Returns total value of inventory

💻 CLI Interface
To run the CLI mode:

bash
Copy
Edit
python main.py
Menu Options:
Add Electronics Product

List All Products

Total Inventory Value

Exit

🌐 Streamlit Web UI
To launch the web app:

bash
Copy
Edit
streamlit run main.py streamlit
Sidebar Actions:
List Products: View all stored products.

Add Product: Input form to add new electronics.

Total Inventory Value: View total worth of inventory.

💾 Session Handling in Streamlit
Inventory state is stored in st.session_state for persistence across interactions.

📌 Dependencies
Python 3.7+

Streamlit

Install required library:

bash
Copy
Edit
pip install streamlit
🚀 Future Improvements
Add delete/update functionality

Filter products by brand or warranty

Save/load inventory from file or database

Authentication for access control
