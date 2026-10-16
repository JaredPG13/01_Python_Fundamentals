item_name = input("Item name? ")
units = input("Units in stock? ")
units = int(units)
reorder_point = input("Reorder point? ")
reorder_point = int(reorder_point)
priority = input("Priority item? (y/n) ")
priority = priority.lower()

print(f"--- Inventory check: {item_name} ---")
print(f"Units in stock: {units}")

if units == 0:
    print("OUT OF STOCK - order immediately")

elif units <= reorder_point:
    print("Reorder needed")

else:
    print("Stock OK")

if priority == "y":
    print("Priority item - notify manager")
