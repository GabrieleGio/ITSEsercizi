from dottore import Dottore
from paziente import Paziente
class Fattura:
    def __init__(self, doctor:Dottore, patient:list[Paziente] = []):
        self.patient = patient
        self.doctor = doctor
        
        if doctor.isAValidDoctor() == True:
            self.fatture = len(self.patient)
            self.salary = 0
        else:
            self.patient = None
            self.doctor = None
            self.fatture = None
            self.salary = None
            print("Non è possibile creare la classe fattura perchè il dottore non è valido")
    
    def getSalary(self):
        self.salary = self.doctor.getParcel() * len(self.patient)
        return self.doctor.getParcel() * len(self.patient)
    
    def getFatture(self):
        return len(self.patient)
    
    def addPatient(self,newPatient:Paziente):
        if newPatient not in self.patient:
            self.patient.append(newPatient)
            self.salary = self.getSalary()
            self.fatture = self.getFatture()
            print(f"Alla lista del Dottor {self.doctor.getName()} è stato aggiunto il paziente {newPatient.getIdCode()}")
        else:
            print("Il paziente è già presente")
    
    def removePatient(self,idCode):
        for paziente in self.patient:
            if paziente.getIdCode() == idCode:
                self.patient.remove(paziente)
                self.salary = self.getSalary()
                self.fatture = self.getFatture()
                print(f"Alla lista del Dottor {self.doctor.getName()} è stato rimosso il paziente {paziente.getIdCode()}")


