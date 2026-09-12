inventory=0
total=0
failed=0

while True:
    user_input=input("Enter a stock quantity (or type 'quit' to exit): ")

    if user_input == 'quit':
        break

    if not user_input.isdigit():

        if user_input.startswith('-') and user_input [1:].isdigit():
            print ("Error: Negative numbers are not allowed. Entry rejected.")
        else:
            print("Error: Invalid input string. Please enter an integer. Entry rejected.")

        failed+=1
        continue
    quantity=int(user_input)
    inventory+=quantity
    total += quantity
    print(f"Current Inventory Total: {inventory}")

    if inventory > 500:
        print("ALERT: Total inventory exceeds 500 units! Overstock limit reached.")
        break

print("\n--- Audit Report ---")
print(f"Total Units Processed: {total}")
print(f"Number of Failed/Rejecteed Entries: {failed}")