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


def find_bread(bread_name):
    return bread_name

print(find_bread("Sourdough"))


def find_shelf_code(item, shelf_code):
    return shelf_code

find_shelf_code("Packing tape", "C-14")
print(find_shelf_code("Packing tape", "C-14"))


def make_drink(drink):
    return drink

order = make_drink("Cold brew")
print(order)
print(order)

ready = make_drink("Iced tea")
print(make_drink("Latte"))
print(ready)


def find_exam_room(patient_name, exam_room):
    return exam_room

patient_room = find_exam_room("Maya", "Room 5")
print(patient_room)
print(patient_room)


def find_order_number(order_number, name_of_packer):
    return order_number

luis_order = find_order_number("Order 1042", "Luis")
kim_order = find_order_number("Order 1043", "Kim")

print(kim_order)
print(luis_order)


def call_customer_name(customer_name, drink):
    return customer_name

name_to_call = call_customer_name("Ava", "Mocha")
print(f"Now calling: {name_to_call}")
print(call_customer_name("Leo", "Chai"))


def seat_guest(guest, table):
    return table

nina_table = seat_guest("Nina", "Table 8")
print(nina_table)