menu = [
    {"drink": "Latte", "price": 4.75},
    {"drink": "Mocha", "price": 5.25},
    {"drink": "Cold brew", "price": 4.50},
]

def save_menu(menu, filename):
    with open(filename, "w") as f:
        for items in menu:
            f.writelines(f"{items['drink']} {items['price']}\n")

save_menu(menu, "menu_check.txt")