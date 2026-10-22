# LOAD: read saved deliveries, or start empty if there's no file yet
try:
    with open("deliveries.txt", "r") as file:
        text = file.read()
    deliveries = text.splitlines()
except FileNotFoundError:
    deliveries = []

# WORK
print(f"Deliveries on file: {len(deliveries)}")