miles = input("How many miles away? ")
miles = float(miles)
if miles < 2:
    print("Delivery fee: $0.00")
elif miles <= 5:
    print("Delivery fee: $3.99")
else:
    print("Sorry, outside delivery range")
