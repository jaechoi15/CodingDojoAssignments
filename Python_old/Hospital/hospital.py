# You're going to build a hospital with patients in it! Create a hospital class.

class Patient(object):
    def __init__(self, id_num, name, allergies):
        self.id = id_num
        self.name = name
        self.allergies = allergies
        self.bed_number = 0
    
    def display_patient(self):
        print "Patient ID #:", self.id
        print "Patient's Name:", self.name
        print "Allergies:", self.allergies
        print "Bed #:", self.bed_number
        print ""
        return self

p1 = Patient(1, "Dwayne", "3s")
p2 = Patient(2, "LeBron", "Durantula")
p3 = Patient(3, "Carmelo", "PhilJ" )
p4 = Patient(4, "Chris", "??")
# p1.display_patient()

class Hospital(object):
    def __init__(self, name):
        self.patients = []
        self.name = name
        self.capacity = 3
    
    def admit(self, p):
        if len(self.patients) < self.capacity:
            self.patients.append(p)
            p.bed_number = len(self.patients)
            print "Admission is complete. Welcome!"
        else:
            print "Sorry, the hospital has reached its maximum capacity."
        return self
    
    def discharge(self, p):
        self.patients.remove(p)
        p.bed_number = 0
        print "You have been discharged. Please exit the building."
        return self
    
    def display_all(self):
        print "Current patients:"
        for i in self.patients:
            i.display_patient()
        return self

Inova = Hospital("Inova")
Inova.admit(p1).admit(p2).admit(p3).discharge(p2).admit(p4).display_all()