def ask_whole_number(question):
    reply = input(question)
    reply = int(reply)
    return reply

people = ask_whole_number("How many people are with patients? ")
print(people + 1)