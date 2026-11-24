def load_pastries(filename):
    pastries = []
    try:
        with open(filename, "r") as f:
            for line in f:
                parts = line.strip().split()
                pastry = {"name": parts[0], "price": float(parts[1])}
                pastries.append(pastry)
    except FileNotFoundError:
        print("No pastry file yet.")
    return pastries

                
def save_pastries(pastries, filename):
    with open(filename, "w") as f:
        for pastry in pastries:
            f.write(f"{pastry['name']} {pastry['price']}\n")

pastries = [{'name': 'Muffin', 'price': 3.25}, {'name': 'Croissant', 'price': 4.00}, {'name': 'Scone', 'price': 2.75}]
save_pastries(pastries, "pastries.txt")
loaded = load_pastries("pastries.txt")
print(loaded)
