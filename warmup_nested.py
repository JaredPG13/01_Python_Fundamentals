total_days = 3
drinks = ["latte", "mocha", "tea", "cold brew"]
day = 1

while day <= total_days:
    print(f"--- Day {day} ---")
    for drink in drinks:
        print(f"How many {drink}s sold?")
    print("Day closed.")
    day = day + 1

print(f"Last drink checked: {drink}")