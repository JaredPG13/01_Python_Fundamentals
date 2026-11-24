def save_plants(plants, filename):
    with open(filename, "w") as f:
        for item in plants:
            f.write(f"{item['plant']} {item['cost']}\n")


def load_plants(filename):
    plants = []
    try:
        with open(filename, "r") as f:
            for line in f:
                parts = line.strip().split()
                plant = {"plant": parts[0], "cost": float(parts[1])}
                plants.append(plant)
    except FileNotFoundError:
        print("No plant file yet.")
    return plants

plants = [{'plant': 'Fern', 'cost': 12.50}, {'plant': 'Cactus', 'cost': 8.00}, {'plant': 'Orchid', 'cost': 24.75}]

save_plants(plants, "plants.txt")
loaded = load_plants("plants.txt")
print(loaded)
missing = load_plants("missing.txt")
print(missing)


def log_sale(plant, cost, filename):
    with open(filename, "a") as f:
        f.write(f"{plant} {cost}\n")

log_sale("Fern", 12.5, "sales_log.txt")
log_sale("Orchid", 24.75, "sales_log.txt")

print(load_plants("sales_log.txt"))