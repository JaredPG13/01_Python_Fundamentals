def ask_whole_number(question):
    got_number = "no"
    while got_number != "yes":
        reply = input(question)
        try:
            reply = int(reply)
            got_number = "yes"
        except ValueError:
            print("Please type a number.")
    return reply

patient_name = input("Patient Name: (or 'end day' to close for day) ")
patients = 0

while patient_name.lower() != "end day":

    print(f"Hello {patient_name}!")
    patients = patients + 1
    new_patient = input("New patient? (y/n) ")
    new_patient = new_patient.lower()
    if new_patient == "y":
        print(f"Ask {patient_name} to fill out the intake form.")

    many_people = ask_whole_number(f"How many people are with {patient_name}? ")
    
    co_pay = ask_whole_number(f"What is {patient_name}'s copay? ")

    minutes_late = ask_whole_number(f"How many minutes late is {patient_name}? ")

    if minutes_late <= 0:
        print(f"Check in {patient_name}!")
    elif minutes_late <= 15:
        print(
            f"Can be seen, but warn {patient_name} that the doctor may be running behind."
        )
    else:
        print(f"{patient_name} will need to reschedule.")

    patient_name = input("Patient Name: (or 'end day' to close for day) ")


print(f"Patients today: {patients}. Check-in closed for the day.")
