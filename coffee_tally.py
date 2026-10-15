def ask_whole_number(question):
    got_number = "no"
    while got_number != "yes":
        reply = input(question)
        try:
            reply = int(reply)
            got_number = "yes"
        except ValueError:
            print("Please type a number.")
    return reply

drink_name = input("Drink name? (or 'close' to close for day) ")
drinks = 0

while drink_name.lower() != "close":
     
    many_drinks = ask_whole_number(f"How many {drink_name}s? ")
    
    print(f"Added {many_drinks} {drink_name}s")

    drinks = drinks + many_drinks
    drink_name = input("Drink name? (or 'close' to close for day) ")

print(f"Cups sold today: {drinks}. Closed for the day. ")