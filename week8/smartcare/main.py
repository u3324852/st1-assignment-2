from domain.patient import Patient
from domain.practitioner import Practitioner
from domain.appointment import AppointmentStatus
from persistence.in_memory_appointment_repository import InMemoryAppointmentRepository
from services.appointment_service import AppointmentService


def main():
    print("SmartCare starting...")

    repo = InMemoryAppointmentRepository()
    service = AppointmentService(repo)

    patient = Patient("P001", "Alice Smith", "alice@example.com")
    doctor = Practitioner("D001", "Dr Jones", "Cardiology")

    appt = service.book_appointment("A001", patient, doctor, "2026-10-10", "10:00")
    print("Booked:", appt.get_details())

    try:
        service.book_appointment("A002", patient, doctor, "2026-10-10", "10:00")
    except ValueError as e:
        print("Duplicate blocked:", e)

    service.cancel_appointment("A001")
    print("After cancel:", appt.status)

    try:
        appt.update_status(AppointmentStatus.COMPLETED)
    except Exception as e:
        print("Illegal transition blocked:", e)


if __name__ == "__main__":
    main()
