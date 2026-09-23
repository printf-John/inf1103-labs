total_inventory = 0
failed_entries = 0

while True:
    user_input = input(
        "Enter stock quantity (or type 'quit' to exit): ").strip()

    if user_input.lower() == 'quit':
        break

    if not user_input.isdigit():
        if user_input.startswith('-'):
            print("Error: Negative numbers are not allowed.")
        else:
            print("Error: Invalid input. Please enter a valid integer.")

        failed_entries += 1
        continue
    quantity = int(user_input)

    total_inventory += quantity
    print(f"Added {quantity} units. Current inventory: {total_inventory}")

    if total_inventory > 500:
        print("ALERT: Overstock limit exceeded (greater than 500 units)!")
        break

print("\n-- Audit Report ---")
print(f"Total Units Processed: {total_inventory}")
print(f"Number of Failed/Rejected Entries: {failed_entries}")
