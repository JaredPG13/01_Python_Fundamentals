patient_name = input("Patient Name: (or 'end day' to close for day) ")

while patient_name.lower() != "end day":

    print(f"Hello {patient_name}!")
    new_patient = input("New patient? (y/n) ")
    new_patient = new_patient.lower()
    if new_patient == "y":
        print(f"Ask {patient_name} to fill out the intake form.")
    
    got_number = "no"
    while got_number != "yes":
        minutes_late = input("How many minutes late is the patient? ")
        try:
            minutes_late = int(minutes_late)
            got_number = "yes"
        except ValueError:
            print("Please type a number")
    if minutes_late <= 0:
        print(f"Check in {patient_name}!")
    elif minutes_late <= 15:
        print(f"Can be seen, but warn {patient_name} that the doctor may be running behind.")
    else:
        print(f"{patient_name} will need to reschedule.")
      
    patient_name = input("Patient Name: (or 'end day' to close for day) ")


print("Check-in closed for the day.")