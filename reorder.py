# ASK item name, store as item
item_name = input("Item name? ")
# ASK units in stock, store as stock
units = input("Units in stock? ")
# CONVERT stock to a whole number
units = int(units)
# ASK reorder point, store as reorder_point
reorder_point = input("Reorder point? ")
# CONVERT reorder_point to a whole number
reorder_point = int(reorder_point)
# ASK priority (y/n), store as priority
priority = input("Priority item? (y/n) ")
# NORMALIZE priority to lowercase
priority = priority.lower()
# SAY the header with the item name
print(f"--- Inventory check: {item_name} ---")
# SAY "Units in stock:" with the stock number
print(f"Units in stock: {units}")
# IF stock is 0
if units == 0:
    #    SAY "OUT OF STOCK - order immediately"
    print("OUT OF STOCK - order immediately")
# OTHERWISE IF stock is at or below reorder_point
elif units <= reorder_point:
    #    SAY "Reorder needed"
    print("Reorder needed")
# OTHERWISE
else:
    #    SAY "Stock OK"
    print("Stock OK")
# IF priority is "y"
if priority == "y":
    #    SAY "Priority item - notify manager"
    print("Priority item - notify manager")
