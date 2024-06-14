from persona import Persona
class Paziente(Persona):
    def __init__(self,first_name: str,last_name: str, code: str):
        super().__init__(first_name,last_name)
        if type(code) == str:
            self.__code = code
        else:
            self.__code = None
            print("Il codice deve essere una stringa!")
    
    def setIdCode(self,idCode):
        if type(idCode) == str:
            self.__code = idCode
        else:
            print("Il codice inserito non è una stringa")

    def getIdCode(self):
        return self.__code
    
    def patientInfo(self):
        nome = self.getName()
        cognome = self.getLastname()
        codice = self.getIdCode()
        return f"Paziente: {nome} {cognome} \nID: {codice}"
    
paziente1 = Paziente("Giovanni","Storti","AA01")
print(paziente1.patientInfo())