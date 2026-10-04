class Patient:
    def __init__(self, patient_id: str, name: str, contact_details: str = ""):
        if not patient_id or not patient_id.strip():
            raise ValueError("patient_id must be non-empty")
        if not name or not name.strip():
            raise ValueError("name must be non-empty")

        self.patient_id = patient_id.strip()
        self.name = name.strip()
        self.contact_details = contact_details.strip() if contact_details else ""

    def update_details(self, name=None, contact_details=None):
        if name is not None:
            if not name.strip():
                raise ValueError("name must be non-empty")
            self.name = name.strip()
        if contact_details is not None:
            self.contact_details = contact_details.strip()

    def get_details(self):
        return {
            "patient_id": self.patient_id,
            "name": self.name,
            "contact_details": self.contact_details,
        }

    def matches_name(self, query: str):
        return query.lower() in self.name.lower()

    def __repr__(self):
        return f"Patient(patient_id={self.patient_id!r}, name={self.name!r})"