class Persona:
    def __init__(self,first_name: str,last_name: str):
        if type(last_name) and type(first_name) == str:
            self.__first_name = first_name
            self.__last_name = last_name
            self.__age = 0
        else:
            self.__first_name = None
            self.__last_name = None
            self.__age = None
            print("Il nome inserito non è una stringa!")
    
    def setName(self,first_name):
        if type(first_name) == str:
            self.__first_name = first_name
        else:
            print("Il nome inserito non è una stringa!")

    def setLastName(self,last_name):
        if type(last_name) == str:
            self.__last_name = last_name
        else:
            print("Il cognome deve essere una stringa")

    def setAge(self,age):
        if type(age) == int:
            self.__age = age
        else:
            print("L'età deve essere un numero intero")

    def getName(self):
        return self.__first_name
    
    def getLastname(self):
        return self.__last_name
    
    def getAge(self):
        return self.__age
    
    def greet(self):
        name = self.getName()
        surname = self.getLastname()
        age = self.getAge()
        return f"Ciao, sono {name} {surname}! Ho {age} anni!"
    
persona1 = Persona("Mario","Rossi")
print(persona1.greet())

