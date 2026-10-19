# define a card called ask_yes_no that takes a question
def ask_yes_no(question):
#   make a flag, start it at no
    got_text = "no"
#   loop while the flag is no:
    while got_text == "no":
#       ask the question, save what they type as reply
        reply = input(question)
#       make the reply lowercase, so "YES" and "Yes" also count
        reply = reply.lower()
#       if the reply is "yes" or "no":
        if reply == "yes" or reply == "no":
#           set the flag to yes
            got_text = "yes"
#       else:
        else:
#           warn them: Please type yes or no
            print("Please type yes or no")
#   hand back reply
    return reply

# start a count of chores done at 0
chores_done = 0
# start the day counter at 1
day_counter = 1
# loop while the day counter is <= 5:
while day_counter <= 5:
#   print which day it is
    print(f"--- Day {day_counter} ---")
#   ask chore 1 with the card, save it as answer
    answer = ask_yes_no("Did you wipe down the bathroom counter? ")
#   if answer is yes:
    if answer == "yes":
#       add +1 to chores done
        chores_done = chores_done + 1

    answer = ask_yes_no("Did you empty the clean dishwasher? ")
    if answer == "yes":
        chores_done = chores_done + 1

    answer = ask_yes_no("Did you put dirty dishes in dishwasher? ")
    if answer == "yes":
        chores_done = chores_done + 1
    day_counter = day_counter + 1
print(f"Chores completed: {chores_done}")

# calculate total for chores missed
chores_missed = 15 - chores_done
# print total
print(f"Chores missed: {chores_missed}")
# calculate percentage completed
percentage_completed = round(chores_done/15 * 100)
# print total
print(f"Completed: {percentage_completed}%")
# if chores completed equals 15
if chores_done == 15:
#   print $10
    print("Allowance: $10")
# otherwise
else:
#   print $0
    print("Allowance: $0")
