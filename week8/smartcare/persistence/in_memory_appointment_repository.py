from domain.appointment import AppointmentStatus
from repositories.appointment_repository import AppointmentRepository


class InMemoryAppointmentRepository(AppointmentRepository):
    def __init__(self):
        self._store = {}

    def add(self, appointment):
        self._store[appointment.appointment_id] = appointment

    def get_by_id(self, appointment_id: str):
        return self._store.get(appointment_id)

    def find_conflicts(self, practitioner_id: str, date: str, time: str):
        return [
            a for a in self._store.values()
            if a.practitioner.practitioner_id == practitioner_id
            and a.date == date
            and a.time == time
            and a.status != AppointmentStatus.CANCELLED
        ]

    def list_by_patient(self, patient_id: str):
        return [
            a for a in self._store.values()
            if a.patient.patient_id == patient_id
        ]

    def list_by_date(self, date: str):
        return [a for a in self._store.values() if a.date == date]

    def list_by_practitioner(self, practitioner_id: str):
        return [
            a for a in self._store.values()
            if a.practitioner.practitioner_id == practitioner_id
        ]