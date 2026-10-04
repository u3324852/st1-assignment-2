from domain.appointment import (
    Appointment,
    AppointmentStatus,
)
from domain.patient import Patient
from domain.practitioner import Practitioner
from repositories.appointment_repository import AppointmentRepository


class AppointmentNotFoundError(Exception):
    pass


class AppointmentService:
    def __init__(self, appointment_repository: AppointmentRepository):
        self._appointments = appointment_repository

    def book_appointment(
        self,
        appointment_id: str,
        patient: Patient,
        practitioner: Practitioner,
        date: str,
        time: str,
    ):
        conflicts = self._appointments.find_conflicts(
            practitioner.practitioner_id, date, time
        )
        if conflicts:
            raise ValueError(
                "Duplicate booking: practitioner already booked at this date and time"
            )

        appointment = Appointment(
            appointment_id=appointment_id,
            patient=patient,
            practitioner=practitioner,
            date=date,
            time=time,
        )
        self._appointments.add(appointment)
        return appointment

    def cancel_appointment(self, appointment_id: str):
        appointment = self._get_or_raise(appointment_id)
        appointment.update_status(AppointmentStatus.CANCELLED)
        self._appointments.add(appointment)
        return appointment

    def complete_appointment(self, appointment_id: str):
        appointment = self._get_or_raise(appointment_id)
        appointment.update_status(AppointmentStatus.COMPLETED)
        self._appointments.add(appointment)
        return appointment

    def get_appointment(self, appointment_id: str):
        return self._get_or_raise(appointment_id)

    def list_patient_history(self, patient_id: str):
        return self._appointments.list_by_patient(patient_id)

    def search_by_date(self, date: str):
        return self._appointments.list_by_date(date)

    def search_by_practitioner(self, practitioner_id: str):
        return self._appointments.list_by_practitioner(practitioner_id)

    def _get_or_raise(self, appointment_id: str):
        appointment = self._appointments.get_by_id(appointment_id)
        if appointment is None:
            raise AppointmentNotFoundError(
                f"Appointment {appointment_id} not found"
            )
        return appointment