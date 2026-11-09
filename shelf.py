def find_reorders(products):
    reorder_names = []
    for product in products:
        if product["quantity"] <= product["reorder_level"]:
            reorder_names.append(product["product_name"])
    return reorder_names

def add_delivery(products, delivery_name, delivery_amount):
    found = False
    for product in products:
        if product["product_name"].lower() == delivery_name.lower():
            product["quantity"] = product["quantity"] + delivery_amount
            found = True
    if not found:
        print(f"{delivery_name} isn't on any shelf. Something's wrong with this delivery.")
    return found


shelf = [
    {"product_name": "Milk", "quantity": 20, "reorder_level": 2, "shelf_location": "P1"},
    {"product_name": "Eggs", "quantity": 5, "reorder_level": 7, "shelf_location": "P2"},
    {"product_name": "Butter", "quantity": 10, "reorder_level": 15, "shelf_location": "P3"},
]

pantry = [
    {"product_name": "Rice", "quantity": 3, "reorder_level": 5, "shelf_location": "P1"},
    {"product_name": "Flour", "quantity": 12, "reorder_level": 4, "shelf_location": "P2"},
    {"product_name": "Pasta", "quantity": 15, "reorder_level": 10, "shelf_location": "P3"},
]

delivery_name = "butter"
delivery_amount = 12

matched = add_delivery(shelf, delivery_name, delivery_amount)

reorder_names = find_reorders(shelf)

for product in shelf:
    print(f"{product['product_name']}: {product['quantity']} on shelf {product['shelf_location']}")

if len(reorder_names) == 0:
    print("No products need reordering")
else:
    if len(reorder_names) == 1:
        noun = "product"
        verb = "needs"
    else:
        noun = "products"
        verb = "need"
    print(f"{len(reorder_names)} {noun} {verb} reordering: {', '.join(reorder_names)}")

add_delivery(pantry, "Rice", 6)
pantry_reorders = find_reorders(pantry)
print(pantry_reorders)