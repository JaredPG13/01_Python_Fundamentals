with open("orders.txt", "a") as f:
    f.write("Flat white\n")
  

with open("orders.txt", "r") as f:
    contents = f.read()

print(contents)

with open("menu.txt", "w") as f:
    f.write("Latte 4.75\n")
    f.write("Mocha 5.25\n")

try:
    with open("menu.txt", "r") as f:
        menu = f.read()
    print(menu)
except FileNotFoundError:
    print("No menu saved yet.")

with open("menu.txt", "r") as f:
    for line in f:
        parts = line.strip().split()
        name = parts[0]
        price = float(parts[1])
        print(f"{name}: ${price}")
        print(price * 2)
