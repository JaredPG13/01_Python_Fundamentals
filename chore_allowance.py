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


# create a list of days Monday-Friday
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
# create a list of chores
chores = ["clean your bathroom", "clean the kitchen", "pick up your room"]
# load saved missed chores, or start empty if there's no file yet
try:
    with open("missed_chores.txt", "r") as file:
        text = file.read()
    missed = text.splitlines()
except FileNotFoundError:
    missed = []
# load days done
try:    
    with open("days_done.txt", "r") as file:
        text = file.read()
    days_done = text.splitlines()
except FileNotFoundError:
    days_done = []
# if days done equals 5 clear days done and missed chores
if len(days_done) == 5:
    days_done = []
    missed = []
# determine what day it is based on how many days done
day = days[len(days_done)]
# print which day it is
print(f"--- {day} ---")
# ask about each chore
for chore in chores:
#   ask each chore
    answer = ask_yes_no(f"Did you {chore}? ")
#   if answer is no:
    if answer == "no":
#       add chore to missed
        missed.append(f"{day}: {chore}")
# add day done
days_done.append(day)
# calculate total chores
total_chores = len(chores) * len(days_done)
# calculate chores done
chores_done = total_chores - len(missed)
# print chores completed total
print(f"Chores completed: {chores_done}")
# calculate total for chores missed
chores_missed = len(missed)
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
# if the week is done
if len(days_done) == 5:
#   if chores done equals total chores
    if chores_done == total_chores:
#       print Allowance: $10
        print("Allowance: $10")
#   otherwise
    else:
#       print Allowance: $0
        print("Allowance: $0")
# midweek
else:
#   if chores done equals total chores
    if chores_done == total_chores:
#       print an encouraging message
        print("You're doing great! Keep it going!")
# save missed chores so they survive after the app closes
with open("missed_chores.txt", "w") as file:
    for missed_chore in missed:
        file.write(f"{missed_chore}\n")
# save days done so they survive after the app closes
with open("days_done.txt", "w") as file:
    for day in days_done:
        file.write(f"{day}\n")