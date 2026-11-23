appointments = [
    {"patient": "Ana", "time": "9:00"},
    {"patient": "Ben", "time": "10:30"},
    {"patient": "Cara", "time": "1:15"},
]


def save_appointments(appointments, filename):
    with open(filename, "w") as f:
        for appointment in appointments:
            f.writelines(f"{appointment['patient']} {appointment['time']}\n")

save_appointments(appointments, "appointments.txt")

def load_appointments(filename):
    appointments = []
    try:
        with open(filename, "r") as f:
            for line in f:
                parts = line.strip().split()
                appointment = {"patient": parts[0], "time": parts[1]}
                appointments.append(appointment)
    except FileNotFoundError:
        print("No appointments saved yet.")
    return appointments
                            
loaded = load_appointments("appointments.txt")
print(loaded)

missing = load_appointments("tomorrow.txt")
print(missing)