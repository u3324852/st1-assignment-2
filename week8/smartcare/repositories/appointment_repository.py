from abc import ABC, abstractmethod


class AppointmentRepository(ABC):
    @abstractmethod
    def add(self, appointment):
        ...

    @abstractmethod
    def get_by_id(self, appointment_id: str):
        ...

    @abstractmethod
    def find_conflicts(self, practitioner_id: str, date: str, time: str):
        ...

    @abstractmethod
    def list_by_patient(self, patient_id: str):
        ...

    @abstractmethod
    def list_by_date(self, date: str):
        ...

    @abstractmethod
    def list_by_practitioner(self, practitioner_id: str):
        ...