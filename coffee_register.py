item_name = input("Enter an order item (or 'close' to exit): ")

# Assumption: The barista must type lowercase 'close' to close the register.

while item_name != "close":
    print(f"Rang up: {item_name}")
    item_name = input("Enter an order item (or 'close' to exit): ")

print("Register closed.")
