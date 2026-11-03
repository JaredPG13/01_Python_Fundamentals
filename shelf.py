shelf = [
    {"product_name": "Milk", "quantity": 2, "reorder_level": 2, "shelf_location": "D2"},
    {"product_name": "Eggs", "quantity": 5, "reorder_level": 7, "shelf_location": "E1"},
    {"product_name": "Butter", "quantity": 10, "reorder_level": 15, "shelf_location": "B3"},
]
reorder_names = []

for product in shelf:
    print(f"{product['product_name']}: {product['quantity']} on shelf {product['shelf_location']}")
    if product["quantity"] <= product["reorder_level"]:
        reorder_names.append(product["product_name"])
        print(f"REORDER: {product['product_name']} is down to {product['quantity']} (reorder level {product['reorder_level']})")

print(f"{len(reorder_names)} products need reordering: {', '.join(reorder_names)}")
