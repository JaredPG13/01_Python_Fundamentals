def greet_customer():
    print("Welcome to Maya's coffee shop.")
    print("What can I get you?")
greet_customer()
greet_customer()

def greet_regular(customer_name):
    print(f"Welcome back, {customer_name}!")
greet_regular("Rosa")
greet_regular("Luis")

def cup_label(customer_name):
    return f"{customer_name}'s order."
label = cup_label("Rosa")
print(label)

greeting = greet_regular("Dana")
print(greeting)

def announce_minutes():
    print(10)

def hand_minutes():
    return 10

a = announce_minutes()
b = hand_minutes()
print(b + 5)
print(a + 5)