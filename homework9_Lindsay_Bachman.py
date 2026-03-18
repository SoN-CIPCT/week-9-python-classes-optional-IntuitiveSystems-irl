# Homework 9 - Python Classes: Medical Record System
# Lindsay Bachman


class Patient:
    """A class to represent a patient in a medical record system."""

    def __init__(self, patient_id, name, age, diagnosis, charges):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.diagnosis = diagnosis
        self.charges = charges

    def display_info(self):
        """Prints the patient's details."""
        print(f"\n--- Patient Record ---")
        print(f"  Patient ID : {self.patient_id}")
        print(f"  Name       : {self.name}")
        print(f"  Age        : {self.age}")
        print(f"  Diagnosis  : {self.diagnosis}")
        print(f"  Charges    : ${self.charges:,.2f}")

    def update_diagnosis(self, new_diagnosis):
        """Updates the patient's diagnosis."""
        old = self.diagnosis
        self.diagnosis = new_diagnosis
        print(f"\n[Updated] {self.name}'s diagnosis changed from '{old}' to '{new_diagnosis}'")

    def add_charges(self, amount):
        """Adds an amount to the patient's charges."""
        self.charges += amount
        print(f"\n[Charge] ${amount:,.2f} added to {self.name}'s bill. New total: ${self.charges:,.2f}")


# --- Create three patient objects ---

patient1 = Patient(1001, "Alice Johnson", 34, "Type 2 Diabetes", 1250.00)
patient2 = Patient(1002, "Brian Lee", 58, "Hypertension", 870.50)
patient3 = Patient(1003, "Carmen Reyes", 45, "Acute Bronchitis", 430.00)

# --- Display patient information ---

print("=" * 40)
print("  MEDICAL RECORD SYSTEM")
print("=" * 40)

patient1.display_info()
patient2.display_info()
patient3.display_info()

# --- Update a patient's diagnosis ---

patient2.update_diagnosis("Hypertension with Hyperlipidemia")

# --- Add charges to a patient's bill ---

patient1.add_charges(350.00)
patient3.add_charges(125.75)

# --- Display updated records ---

print("\n" + "=" * 40)
print("  UPDATED RECORDS")
print("=" * 40)

patient1.display_info()
patient2.display_info()
patient3.display_info()

# --- Bonus: Store patients in a list and print all records ---

print("\n" + "=" * 40)
print("  BONUS: ALL PATIENT RECORDS")
print("=" * 40)

patients = [patient1, patient2, patient3]

for patient in patients:
    patient.display_info()
