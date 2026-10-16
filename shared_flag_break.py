#make a flag, start it at "no"
ok = "no"
received = 0
damaged = 0
#loop while the flag is "no":
while ok == "no":
#   try:
    try:
#       ask for pallets received
        pallets_received = input("Pallets received? ")
#       convert it to a whole number
        pallets_received = int(pallets_received)
        received = pallets_received
#       set the flag to "yes"
        ok = "yes"
#   if it fails with ValueError:
    except ValueError:
#       warn them
        print("Please type a number.")

ok = "no"
#loop while the flag is "no":
while ok == "no":
#   try:
    try:
#       ask for pallets damaged
        pallets_damaged = input("Pallets damaged? ")
#       convert it to a whole number
        pallets_damaged = int(pallets_damaged)
        damaged = pallets_damaged
#       set the flag to "yes"
        ok = "yes"
#   if it fails with ValueError:
    except ValueError:
#       warn them
        print("Please type a number")

#print totals for both received and damaged numbers 
print(f"Received: {received}, Damaged: {damaged}")