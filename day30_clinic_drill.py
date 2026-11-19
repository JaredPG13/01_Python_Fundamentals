appointments = [
    {"patient": "Maria Lopez", "doctor": "Dr. Patel", "room": 3},
    {"patient": "James Carter", "doctor": "Dr. Nguyen", "room": 5},
    {"patient": "Aisha Khan", "doctor": "Dr. Patel", "room": 1},
]


def find_patient_room(appointments, patient_name):
    for appointment in appointments:
        if appointment["patient"] == patient_name:
            return appointment["room"]
    return "Not found"

print(find_patient_room(appointments, "Maria Lopez"))
print(find_patient_room(appointments, "Aisha Khan"))
print(find_patient_room(appointments, "Tom Reed"))

room = find_patient_room(appointments, "James Carter")

print(f"James Carter is waiting in room {room}")
