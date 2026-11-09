def check_in(appointments, patient_name):
    found = False
    for appointment in appointments:
        if appointment["patient_name"].lower() == patient_name.lower():
            appointment["checked_in"] = True
            found = True
    if not found:
        print(f"{patient_name} doesn't have an appointment scheduled")
    return found
            
def find_waiting(appointments):
    waiting_names = []
    for appointment in appointments:
        if not appointment["checked_in"]:
            waiting_names.append(appointment["patient_name"])
    return waiting_names


appointments = [
    {"patient_name": "Adam", "time": "9:30", "doctor": "Dr. Johnson", "checked_in": True},
    {"patient_name": "Bob", "time": "10:00", "doctor": "Dr. Kim", "checked_in": True},
    {"patient_name": "Charlie", "time": "10:30", "doctor": "Dr. Chang", "checked_in": False},
    {"patient_name": "Dan", "time": "11:00", "doctor": "Dr. Misty", "checked_in": False},
]

check_in(appointments, "charlie")
check_in(appointments, "Eden")

print(find_waiting(appointments))