from abc import ABC, abstractmethod
import math

class Forma(ABC):
    @abstractmethod
    def getArea(self):
        pass

    @abstractmethod
    def render(self):
        pass

class Quadrato(Forma):
    def __init__(self,lato):
        if lato <= 0:
            raise ValueError("Il lato deve essere maggiore di 0!")
        else:
            self.lato = lato

    def getArea(self):
        return self.lato * 4
    
    def render(self):
        print("*" * self.lato)
        for i in range(2,self.lato):
            print("*",end=" " * (self.lato-2)+"*\n")
        print("*" * self.lato)
        
class Rettangolo(Forma):
    def __init__(self,base, altezza):
        if base <= 0 or altezza <= 0:
            raise ValueError("La base e l'altezza devono essere maggiori di 0!")
        else:
            self.base = base
            self.altezza = altezza

    def getArea(self):
        return self.base * self.altezza
    
    def render(self):
        print("*" * self.base)
        if self.base == 1:
            for i in range(2,self.altezza):
                print("*")
        else:
            for i in range(2,self.altezza):
                print("*",end=" " * (self.base-2)+"*\n")
        print("*" * self.base)

class Triangolo(Forma):
    def __init__(self,cateto1,cateto2):
        if cateto2 > cateto1:
            cateto2,cateto1 = cateto1,cateto2
            
        if cateto1 <= 0 or cateto2 <= 0:
            raise ValueError("I cateti devono essere maggiori di 0!")
        else:
            self.cateto1 = cateto1
            self.cateto2 = cateto2
            self.ipotenusa = math.sqrt(self.cateto1**2 + self.cateto2**2)

    def getArea(self):
        return (self.cateto1 * self.cateto2) / 2
    
    def render(self):
        print("*")
        for i in range(2,self.cateto2):
            print("*",end=" " * (i-1) +"*\n")
        print("*" * self.cateto1)


quadrato1 = Quadrato(7)
quadrato1.render()
print()
print()
rettangolo1 = Rettangolo(8,6)
rettangolo1.render()
print()
print()
triangolo1 = Triangolo(7,5)
triangolo1.render()
print()
print()
rettangoloerrore = Rettangolo(1,5)
rettangoloerrore.render()
print()
print()
triangoloerrore = Triangolo(4,4)
triangoloerrore.render()