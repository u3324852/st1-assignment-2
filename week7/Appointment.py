from __future__ import annotations
from enum import Enum
from typing import Optional


class AppointmentStatus(Enum):
    BOOKED = "Booked"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"


class InvalidStatusTransitionError(Exception):
    pass


class Appointment:
    def __init__(
        self,
        appointment_id: str,
        patient: Patient,
        practitioner: Practitioner,
        date: str,
        time: str,
        status: AppointmentStatus = AppointmentStatus.BOOKED,
    ):
        if not appointment_id or not appointment_id.strip():
            raise ValueError("appointment_id must be non-empty")
        if not isinstance(patient, Patient):
            raise TypeError("patient must be a Patient instance")
        if not isinstance(practitioner, Practitioner):
            raise TypeError("practitioner must be a Practitioner instance")
        if not date or not date.strip():
            raise ValueError("date must be non-empty")
        if not time or not time.strip():
            raise ValueError("time must be non-empty")
        if not isinstance(status, AppointmentStatus):
            raise TypeError("status must be an AppointmentStatus")

        self.appointment_id = appointment_id.strip()
        self.patient = patient
        self.practitioner = practitioner
        self.date = date.strip()
        self.time = time.strip()
        self._status = status

    @property
    def status(self) -> AppointmentStatus:
        return self._status

    def update_status(self, new_status: AppointmentStatus) -> None:
        if not isinstance(new_status, AppointmentStatus):
            raise TypeError("new_status must be an AppointmentStatus")

        if self._status == AppointmentStatus.CANCELLED:
            raise InvalidStatusTransitionError("Cannot change a cancelled appointment")
        if self._status == AppointmentStatus.COMPLETED:
            raise InvalidStatusTransitionError("Cannot change a completed appointment")

        if self._status == AppointmentStatus.BOOKED:
            if new_status in (AppointmentStatus.COMPLETED, AppointmentStatus.CANCELLED):
                self._status = new_status
            else:
                raise InvalidStatusTransitionError(
                    f"Cannot transition from {self._status.value} to {new_status.value}"
                )
        else:
            raise InvalidStatusTransitionError(f"Invalid current status: {self._status}")

    def is_duplicate_for(
        self,
        practitioner: Practitioner,
        date: str,
        time: str
    ) -> bool:
        return (
            self.practitioner.practitioner_id == practitioner.practitioner_id
            and self.date == date.strip()
            and self.time == time.strip()
            and self._status != AppointmentStatus.CANCELLED
        )

    def get_details(self) -> dict:
        return {
            "appointment_id": self.appointment_id,
            "patient": self.patient.get_details(),
            "practitioner": self.practitioner.get_details(),
            "date": self.date,
            "time": self.time,
            "status": self._status.value,
        }

    def __repr__(self) -> str:
        return f"Appointment(id={self.appointment_id!r}, status={self._status.value!r})"
