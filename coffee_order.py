#ASK how many drinks
#CONVERT drinks to a whole number
#SET cost to $4
#MULTIPLY drinks by cost of drink and store it as total
#IF drinks is 5 or more
#          SUBTRACT $2 from total
#SAY total

drinks = input("How many drinks? ")
drinks = int(drinks)
cost = 4
total = drinks * cost
if drinks >= 5:
    total = total - 2
print(total)