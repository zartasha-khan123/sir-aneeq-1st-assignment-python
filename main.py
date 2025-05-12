# Inventory Management System
import streamlit as st

# =============================
# Core Classes
# =============================

class Product:
    def __init__(self, pid, name, price, quantity):
        self.pid = pid
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.pid}: {self.name} (${self.price}) x {self.quantity}"


class Electronics(Product):
    def __init__(self, pid, name, price, quantity, warranty_years, brand):
        super().__init__(pid, name, price, quantity)
        self.warranty_years = warranty_years
        self.brand = brand

    def __str__(self):
        return (f"{super().__str__()} | Brand: {self.brand}, "
                f"Warranty: {self.warranty_years} years")


class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.pid in self.products:
            self.products[product.pid].quantity += product.quantity
        else:
            self.products[product.pid] = product

    def list_all_products(self):
        return list(self.products.values())

    def total_inventory_value(self):
        return sum(p.total_value() for p in self.products.values())


# =============================
# Streamlit UI
# =============================

def run_streamlit_ui():
    st.title("📦 Inventory Management System")

    # ✅ Persistent Inventory using Session State
    if 'inventory' not in st.session_state:
        st.session_state.inventory = Inventory()

    inventory = st.session_state.inventory

    st.sidebar.header("Actions")
    action = st.sidebar.selectbox("Choose Action", ["List Products", "Add Product", "Total Inventory Value"])

    if action == "List Products":
        st.subheader("All Products")
        products = inventory.list_all_products()
        if not products:
            st.info("No products in inventory.")
        else:
            for p in products:
                st.text(str(p))

    elif action == "Add Product":
        st.subheader("Add New Electronics Product")

        pid = st.text_input("Product ID")
        name = st.text_input("Name")
        price = st.number_input("Price", min_value=0.0)
        quantity = st.number_input("Quantity", min_value=0)
        warranty = st.number_input("Warranty (years)", min_value=0)
        brand = st.text_input("Brand")

        if st.button("Add Product"):
            if pid and name and brand:
                try:
                    product = Electronics(pid, name, price, quantity, warranty, brand)
                    inventory.add_product(product)
                    st.success(f"✅ Product '{name}' added successfully!")
                except Exception as e:
                    st.error(f"Error: {e}")
            else:
                st.warning("⚠️ Please fill all required fields.")

    elif action == "Total Inventory Value":
        total = inventory.total_inventory_value()
        st.metric("Total Inventory Value", f"${total:.2f}")


# =============================
# CLI Interface
# =============================

def run_cli():
    inventory = Inventory()

    while True:
        print("\nInventory Management")
        print("1. Add Electronics Product")
        print("2. List All Products")
        print("3. Total Inventory Value")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            pid = input("Product ID: ")
            name = input("Name: ")
            price = float(input("Price: "))
            qty = int(input("Quantity: "))
            warranty = int(input("Warranty (years): "))
            brand = input("Brand: ")

            product = Electronics(pid, name, price, qty, warranty, brand)
            inventory.add_product(product)
            print("✅ Product added successfully.")

        elif choice == "2":
            print("\n--- All Products ---")
            for p in inventory.list_all_products():
                print(p)

        elif choice == "3":
            print(f"💰 Total Value: ${inventory.total_inventory_value():.2f}")

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice.")


# =============================
# Entry Point
# =============================

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "streamlit":
        run_streamlit_ui()
    else:
        run_cli()
