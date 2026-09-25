def get_valid_input():
    user_input = input(
        "Enter stock quantity (or type 'quit' to exit): "
    ).strip()

    if user_input.lower() == "quit":
        return "quit"

    if not user_input.isdigit():
        if user_input.startswith("-"):
            print("Error: Negative numbers are not allowed.")
        else:
            print("Error: Invalid input. Please enter a valid integer.")

        return None

    return int(user_input)


def process_delivery(current_total, new_value):
    return current_total + new_value


def calculate_tax(amount):
    return amount * 0.10


def generate_report(total_units, failed_attempts):
    print("\n-- Audit Report ---")
    print(f"Total Units Processed: {total_units}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")


def main():
    total_inventory = 0
    failed_entries = 0

    while True:
        quantity = get_valid_input()

        if quantity == "quit":
            break

        if quantity is None:
            failed_entries += 1
            continue

        total_inventory = process_delivery(
            total_inventory,
            quantity
        )

        tax = calculate_tax(quantity)

        print(
            f"Added {quantity} units. "
            f"Current inventory: {total_inventory}"
        )

        print(f"Tax for this delivery: {tax:.2f}")

        if total_inventory > 500:
            print(
                "ALERT: Overstock limit exceeded "
                "(greater than 500 units)!"
            )
            break

    generate_report(
        total_inventory,
        failed_entries
    )


if __name__ == "__main__":
    main()
