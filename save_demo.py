orders = ["latte", "mocha", "tea"]

with open("orders_log.txt", "a") as file:
    for order in orders:
        file.write(f"{order}\n")