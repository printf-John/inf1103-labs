
# inventory_manager.py

import json
import os

INVENTORY_FILE = os.environ.get(
    "INVENTORY_FILE", "inventory.json"
)


def load_inventory():
    """Load products from the JSON file."""

    if not os.path.exists(INVENTORY_FILE):
        print("Inventory file not found. Starting with empty inventory.")
        return []

    try:
        with open(INVENTORY_FILE, "r", encoding="utf-8") as file:
            inventory = json.load(file)

        if not isinstance(inventory, list):
            print("Error: Inventory data must be a list.")
            return []

        required_fields = {"id", "name", "price", "stock"}
        seen_ids = set()

        for product in inventory:
            if not isinstance(product, dict):
                print("Error: Invalid product record.")
                return []

            if not required_fields.issubset(product):
                print("Error: Product record is missing fields.")
                return []

            if not isinstance(product["id"], str) or not product["id"].strip():
                print("Error: Invalid product ID.")
                return []

            if product["id"] in seen_ids:
                print("Error: Duplicate product ID in inventory.")
                return []

            if not isinstance(product["name"], str) or not product["name"].strip():
                print("Error: Invalid product name.")
                return []

            if (
                isinstance(product["price"], bool)
                or not isinstance(product["price"], (int, float))
                or product["price"] < 0
            ):
                print("Error: Invalid product price.")
                return []

            if (
                isinstance(product["stock"], bool)
                or not isinstance(product["stock"], int)
                or product["stock"] < 0
            ):
                print("Error: Invalid stock quantity.")
                return []

            seen_ids.add(product["id"])

        print("inventory.json found.")
        print("Inventory loaded successfully.")
        return inventory

    except json.JSONDecodeError:
        print("Error: inventory.json contains invalid JSON.")
        return []

    except OSError as error:
        print(f"Error reading inventory: {error}")
        return []


def save_inventory(inventory):
    """Save the inventory list to JSON."""

    try:
        with open(INVENTORY_FILE, "w", encoding="utf-8") as file:
            json.dump(inventory, file, indent=4)

        print("Inventory saved successfully to inventory.json.")
        return True

    except (OSError, TypeError, ValueError) as error:
        print(f"Error saving inventory: {error}")
        return False


def get_non_empty_input(prompt):
    """Ask until the user enters a non-empty value."""

    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("Input cannot be empty. Please try again.")


def get_non_negative_float(prompt):
    """Read a non-negative price."""

    while True:
        try:
            value = float(input(prompt).strip())

            if value < 0:
                print("Value cannot be negative.")
            else:
                return value

        except ValueError:
            print("Invalid input. Please enter a number.")


def get_non_negative_int(prompt):
    """Read a non-negative whole number."""

    while True:
        try:
            value = int(input(prompt).strip())

            if value < 0:
                print("Value cannot be negative.")
            else:
                return value

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def add_product(inventory):
    """Add a new product to the inventory."""

    print("\nAdd New Product")

    product_id = get_non_empty_input("Product ID: ").upper()

    if search_product(inventory, product_id, display=False):
        print("Product ID already exists.")
        return

    name = get_non_empty_input("Product Name: ")
    price = get_non_negative_float("Price: ")
    stock = get_non_negative_int("Stock Quantity: ")

    product = {
        "id": product_id,
        "name": name,
        "price": price,
        "stock": stock
    }

    inventory.append(product)
    print("Product added successfully!")


def update_stock(inventory):
    """Update an existing product's stock quantity."""

    print("\nUpdate Stock")
    product_id = get_non_empty_input("Enter Product ID: ").upper()

    product = search_product(inventory, product_id, display=False)

    if product is None:
        print("Product not found.")
        return

    print("Product Found:")
    print(f"Name: {product['name']}")
    print(f"Current Stock: {product['stock']}")

    new_stock = get_non_negative_int("New Stock Quantity: ")
    product["stock"] = new_stock

    print("Stock updated successfully!")


def search_product(inventory, product_id, display=True):
    """Find a product by ID."""

    for product in inventory:
        if product["id"].upper() == product_id.upper():
            if display:
                print("\nProduct Found")
                print("-" * 40)
                print(f"ID: {product['id']}")
                print(f"Name: {product['name']}")
                print(f"Price: ${product['price']:.2f}")
                print(f"Stock: {product['stock']}")
                print("-" * 40)

            return product

    if display:
        print("Product not found.")

    return None


def display_all(inventory):
    """Display every product."""

    print("\nCurrent Inventory")
    print("-" * 65)

    if not inventory:
        print("No products in inventory.")
    else:
        for product in inventory:
            print(
                f"ID: {product['id']} | "
                f"Name: {product['name']} | "
                f"Price: ${product['price']:.2f} | "
                f"Stock: {product['stock']}"
            )

    print("-" * 65)


def display_menu():
    """Display the main menu."""

    print("\n----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")


def main():
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)

    inventory = load_inventory()

    while True:
        display_menu()
        option = input("Enter option: ").strip()

        if option == "1":
            display_all(inventory)

        elif option == "2":
            add_product(inventory)

        elif option == "3":
            update_stock(inventory)

        elif option == "4":
            product_id = get_non_empty_input(
                "Enter Product ID: "
            ).upper()
            search_product(inventory, product_id)

        elif option == "5":
            print("Saving inventory...")
            save_inventory(inventory)

        elif option == "6":
            print("Saving inventory before exit...")

            if save_inventory(inventory):
                print("Thank you for using Inventory Management System.")
                print("Program terminated.")
                break

            print("Exit cancelled because saving failed.")

        else:
            print("Invalid option. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
