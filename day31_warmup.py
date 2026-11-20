menu = [
    {"drink": "Latte", "size": "Medium", "price": 4.75},
    {"drink": "Cold brew", "size": "Large", "price": 5.25},
    {"drink": "Chai tea", "size": "Small", "price": 3.50},
]


def find_drink_price(menu, drink_name):
    for item in menu:
        if item["drink"] == drink_name:
            return item["price"]
    return "Not found"

print(find_drink_price(menu, "Latte"))
print(find_drink_price(menu, "Chai tea"))
print(find_drink_price(menu, "Slow drip"))


price = find_drink_price(menu, "Cold brew")
print(f"Cold brew: ${price}")