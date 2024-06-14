from persona import Persona

class Dottore(Persona):
    def __init__(self,first_name: str,last_name: str,specialization: str,parcel: float):
        super().__init__(first_name,last_name)
        if type(specialization) == str:
            self.__specialization = specialization
        else:
            self.__specialization = None
            print("La specializzazione deve essere una stringa!")
        
        if type(parcel) == float:
            self.__parcel = parcel
        else:
            self.__parcel = None
            print("La parcella deve essere un numero!")
    

    def DoctorGreet(self):
        stringa = self.greet()
        specializzazione = self.getSpecialization()
        parcella = self.getParcel()
        return f"{stringa} La mia specializzazione è {specializzazione} e la mia parcella è {parcella}"


    def setSpecialization(self,specialization):
        if type(specialization) == str:
            self.__specialization = specialization
        else:
            print("La specializzazione deve essere una stringa!")

    def setParcel(self,parcel):
        if type(parcel) == float:
            self.__parcel = parcel
        else:
            print("La parcella deve essere un numero!")

    def getSpecialization(self):
        return self.__specialization
    
    def getParcel(self):
        return self.__parcel
    
    def isAValidDoctor(self):
        age = self.getAge()
        nome = self.getName()
        cognome = self.getLastname()
        if age >= 30:
            print(f"Doctor {nome} {cognome} is a valid doctor.")
        else:
            print(f"Doctor {nome} {cognome} is NOT a valid doctor!")

dottore1 = Dottore("Francesco","Totti","Pediatra",321.00)
dottore1.setAge(41)
dottore2 = Dottore("Mario","Sturniolo","Chirurgo",25.00)
dottore2.setAge(26)
dottore1.DoctorGreet()
dottore2.DoctorGreet()
dottore1.isAValidDoctor()
dottore2.isAValidDoctor()

        