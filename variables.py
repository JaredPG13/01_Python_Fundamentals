drink = "latte"
print(drink)
print("drink")
print("I ordered a", drink)
shop_name = "Bean Counter"
cups_sold = 142
price = 4.75
is_open = True

print(type(shop_name))
print(type(cups_sold))
print(type(price))
print(type(is_open))

revenue = cups_sold * price
print("Revenue:", revenue)
print(type(revenue))
print(142 + 8)
print("142" + "8")
quantity = "3"
price = 4.75
total = int(quantity) * price
print(f"Revenue: ${revenue:.2f}")
print(f"{shop_name} sold {cups_sold} cups today")
print(f"Order total: ${total:.2f}")
