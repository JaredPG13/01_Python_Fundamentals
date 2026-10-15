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

pallets = ask_whole_number("How many pallets arrived? ")
print(pallets + 1)