# LOAD: read saved orders from the file
with open("orders_log.txt", "r") as file:
    text = file.read()
orders = text.splitlines()

# WORK: use the list
print(f"Orders on file: {len(orders)}")
for order in orders:
    print(order)