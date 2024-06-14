from dottore import Dottore
from paziente import Paziente
class Fattura:
    def __init__(self,patient:list = [] ,doctor: list = []):
        self.patient = patient
        self.doctor = doctor

        for dottore in self.doctor:
            if dottore.isAValidDoctor() == True:
                self.fatture = len(self.patient)
                self.salary = 0
            else:
                self.patient = None
                self.doctor = None
                self.fatture = None
                self.salary = None
                print("Non è possibile creare la classe fattura perchè il dottore non è valido")
                break
    
    def getSalary(self):
        return s

