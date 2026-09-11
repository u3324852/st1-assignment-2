##### TASK 1 #####
'''
print("welcome to smartCare: Community clinic Appointment Booking System")

#appointment 1
patient1_name = ("Jack Smith")
practitioner1_name = ("Dr Garry Jones")
Appointment1_time = "2026-9-3 11:00am"
print("\n\nAPPOINTMENT 1 \nPatient: " + patient1_name + "\nPractitioner: " + practitioner1_name + "\nAppointment Time: " + Appointment1_time)

#appointment 2
patient2_name = ("Mary Wilson")
practitioner2_name = ("Dr Alice Brown")
Appointment2_time = "2026-9-5 9:30am"
print("\n\nAPPOINTMENT 2 \nPatient: " + patient2_name + "\nPractitioner: " + practitioner2_name + "\nAppointment Time: " + Appointment2_time)


##### TASK 1 ENHANCED #####


appointments = []

def book_appointment(patient_name, practitioner_name, appointment_time):
    if not patient_name:
        print("patient name cannot be empty")
    appointment = {
        "Patient": patient_name,
        "Practitioner": practitioner_name,
        "Time": appointment_time
    }
    appointments.append(appointment)

def display_appointments():
    if not appointments:
        print("No appointments recorded")
        return
    for appointment in appointments:
        print(f"\n\nAPPOINTMENT \nPatient: {appointment["Patient"]} \nPractitioner: {appointment["Practitioner"]} \nAppointment Time: {appointment['Time']}")

book_appointment("Jack Smith", "Dr Garry Jones", "2026-9-3 11:00am")
book_appointment("Mary Wilsom", "Dr Alice Brown", "2026-9-5 9:30am")
display_appointments()
'''

##### AI CODE ####

appointments = []

def book_appointment(patient_name, practitioner_name, appointment_time):
    appointment = {
        "Patient": patient_name,
        "Practitioner": practitioner_name,
        "Time": appointment_time
    }

    appointments.append(appointment)

# Book an appointment
book_appointment("Jack Smith", "Dr Garry Jones", "2026-09-11 11:00am")

# Display the appointment
print(appointments)
