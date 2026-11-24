def log_visit(pet, weight, filename):
    with open(filename, "a") as f:
        f.write(f"{pet} {weight}\n")

log_visit("Biscuit", 22.5, "visits.txt")
log_visit("Pepper", 9.75, "visits.txt")