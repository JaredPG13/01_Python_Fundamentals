def brew_house_coffee():
    print("Grinding beans...")
    print("Brewing...")
    print("House coffee ready.")

brew_house_coffee()
brew_house_coffee()


def announce_closing():
    print("The clinic closes in 15 minutes.")
    print("Please check out at the front desk.")

announce_closing()


def open_bakery():
    print("Lights on")
    print("Ovens heating")
    print("Doors unlocked")

open_bakery()
open_bakery()


def serve_drink(drink):
    print("Dispensing...")
    print(drink)

serve_drink("Iced tea")
serve_drink("Lemonade")


def where_to_go(shelf_code):
    print("Next stop:")
    print(shelf_code)

where_to_go("A-12")
where_to_go("C-04")


def label_order(customer, drink):
    print("Order for:")
    print(customer)
    print("Drink:")
    print(drink)

label_order("Maria", "Latte")
label_order("Sam", "Mocha")


def send_reminder(patient, doctor):
    print("Reminder for:")
    print(patient)
    print("Your doctor:")
    print(doctor)

send_reminder("Ana", "Dr. Patel")
send_reminder("Ben", "Dr. Lopez")


def todays_special():
    return "Pumpkin latte"

todays_special()
print(todays_special())


def show_special():
    print("Pumpkin latte")


def give_special():
    return "Pumpkin latte"

show_special()
give_special()


def find_dock():
    return "Dock 7"

find_dock()
print(find_dock())