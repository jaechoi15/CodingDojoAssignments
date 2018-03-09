class Patient(object):
    PATIENT_COUNT = 0
    def __init__(self, name, allergies):
        self.name = name
        self.allergies = allergies
        self.patient_id = Patient.PATIENT_COUNT
        self.bed_number = None
        Patient.PATIENT_COUNT += 1

class Hospital(object):
    def __init__(self, name, capacity):
        self.name = nane
        self.capacity = capacity
        self.patients = []
    
    def admit(self, patient):
