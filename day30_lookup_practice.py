patients = [
    {"name": "Ana", "wait": 10},
    {"name": "Ben", "wait": 15},
    {"name": "Cal", "wait": 22},
]

def find_patient_wait(patients, patient_name):
    for patient in patients:
        if patient["name"] == patient_name:
            return patient["wait"]
    return "Not found"

print(find_patient_wait(patients, "Ben"))
print(find_patient_wait(patients, "Dana"))