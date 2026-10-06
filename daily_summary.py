report_name = "=== Bean Counter: Daily Summary ==="
print(report_name)
date = "Date: October 5, 2026"
print(date)
latte_sold = 86
latte_price = 4.75
latte_total = latte_sold * latte_price
print(f"Lattes: {latte_sold} sold, ${latte_total:.2f}")
drip_sold = 56
drip_price = 2.50
drip_total = drip_sold * drip_price
print(f"Drip coffee: {drip_sold} sold, ${drip_total:.2f}")
pastries_sold = 40
pastries_price = 3.25
pastries_total = pastries_sold * pastries_price
print(f"Pastries: {pastries_sold} sold, ${pastries_total:.2f}")
items_sold = latte_sold + drip_sold + pastries_sold
print("Items sold:", items_sold)
sales_total = latte_total + drip_total + pastries_total
print(f"Sales total: ${sales_total:.2f}")
tips = "63.40"
tips = float(tips)
print(f"Tips: ${tips:.2f}")
grand_total = latte_total + drip_total + pastries_total + tips
print(f"Grand total: ${grand_total:.2f}")
