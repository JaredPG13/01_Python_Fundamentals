# define a card called ask_yes_no that takes a question
def ask_yes_no(question):
#   make a flag, start it at no
    question_answered = "no"
#   loop while the flag is no
    while question_answered == "no":
#       ask the question, save what they type as reply
        reply = input(question)
#       make the reply lowercase, so "YES" and "Yes" also count
        reply = reply.lower()
#       if the reply is "yes" or "no":
        if reply == "yes" or reply == "no":
#           set the flag to yes
            question_answered = "yes"
#       else:
        else:
#           warn them: Please type yes or no
            print("Please type yes or no")
#   hand back reply
    return reply


# start a count of chores done at 0
chores_done = 0
# create a list of days Monday-Friday
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
# create a list of chores
chores = ["clean your bathroom", "clean the kitchen", "pick up your room"]
# total = number of chores x number of days
total_chores = len(chores) * len(days)
# load saved missed chores, or start empty if there's no file yet
try:
    with open("missed_chores.txt", "r") as file:
        text = file.read()
    missed = text.splitlines()
except FileNotFoundError:
    missed = []
# go through each day of the week
for day in days:
#   print which day it is
    print(f"--- {day} ---")
#   ask about each chore
    for chore in chores:
#       ask each chore
        answer = ask_yes_no(f"Did you {chore}? ")
#       if answer is yes:
        if answer == "yes":
#           add +1 to chores done
            chores_done = chores_done + 1
#       otherwise
        else:
#           add missed chore
            missed.append(f"{day}: {chore}")

# print chores completed total
print(f"Chores completed: {chores_done}")
# calculate total for chores missed
chores_missed = total_chores - chores_done
# print chores missed total
print(f"Chores missed: {chores_missed}")
# if chores missed equals 0
if chores_missed == 0:
#   print encouraging message
    print("You completed all chores! Great job!")
# otherwise
else:
#   print what day and chore was missed
    print("You missed:")
#   list each missed chore
    for missed_chore in missed:
        print(missed_chore)
# calculate percentage completed
percentage_completed = round(chores_done / total_chores * 100)
# print chores completed percentage
print(f"Completed: {percentage_completed}%")
# if chores completed equals total chores
if chores_done == total_chores:
#   print $10
    print("Allowance: $10")
# otherwise
else:
#   print $0
    print("Allowance: $0")
# save missed chores so they survive after the app closes
with open("missed_chores.txt", "w") as file:
    for missed_chore in missed:
        file.write(f"{missed_chore}\n")