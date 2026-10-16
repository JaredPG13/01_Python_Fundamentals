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