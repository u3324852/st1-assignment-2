class Practitioner:
    def __init__(self, practitioner_id: str, name: str, specialty: str = "General"):
        if not practitioner_id or not practitioner_id.strip():
            raise ValueError("practitioner_id must be non-empty")
        if not name or not name.strip():
            raise ValueError("name must be non-empty")

        self.practitioner_id = practitioner_id.strip()
        self.name = name.strip()
        self.specialty = specialty.strip() if specialty else "General"

    def update_details(self, name=None, specialty=None):
        if name is not None:
            if not name.strip():
                raise ValueError("name must be non-empty")
            self.name = name.strip()
        if specialty is not None:
            self.specialty = specialty.strip() if specialty else "General"

    def get_details(self):
        return {
            "practitioner_id": self.practitioner_id,
            "name": self.name,
            "specialty": self.specialty,
        }

    def __repr__(self):
        return f"Practitioner(practitioner_id={self.practitioner_id!r}, name={self.name!r})"
