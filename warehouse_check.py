bins = ["bin A", "bin B", "bin C"]

try:
    with open("checked_bins.txt", "r") as file:
        text = file.read()
    bins_checked = text.splitlines()
except FileNotFoundError:
    bins_checked = []

bin = bins[len(bins_checked)]
bins_checked.append(bin)

print(f"Checking {bin}")
print(bins_checked)

with open("checked_bins.txt", "w") as file:
    for bin in bins_checked:
        file.write(f"{bin}\n")