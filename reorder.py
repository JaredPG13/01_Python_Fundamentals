def ask_whole_number(question):
    has_number = "no"
    while has_number != "yes":
        reply = input(question)
        try:
            reply = int(reply)
            has_number = "yes"
        except ValueError:
            print("Please type a number.")
    return reply

item_name = input("Item name? ")
units = ask_whole_number("Units in stock? ")
reorder_point = ask_whole_number("Reorder point? ")
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
