#Da finire
from abc import ABC, abstractmethod

class CodificatoreMessaggio(ABC):
    @abstractmethod
    def codifica(self, testoInChiaro: str) -> str:
        pass

class DecodificatoreMessaggio(ABC):
    @abstractmethod
    def decodifica(self, testoCodificato: str) -> str:
        pass

class CifratoreAScorrimento(CodificatoreMessaggio,DecodificatoreMessaggio):
    def __init__(self, chiave: int):
        self.chiave = chiave
    
    def codifica(self, testoInChiaro: str) -> str:
        testoInChiaro = testoInChiaro.lower()
        testoInChiaro = list(testoInChiaro)
        alfabeto = "abcdefghijklmnopqrstuvwxyz"
        alfabeto = list(alfabeto)
        nuovotesto = []
        for lettera in testoInChiaro:
            if lettera in alfabeto:
                posizione = alfabeto.index(lettera)
                nuovaposizione = posizione+self.chiave
                if nuovaposizione<=len(alfabeto):
                    nuovotesto.append(alfabeto[nuovaposizione])
                else:
                    nuovaposizione=nuovaposizione-len(alfabeto)
                    nuovotesto.append(alfabeto[nuovaposizione])
        return nuovotesto
    
    def decodifica(self, testoCodificato: str) -> str:
        testoCodificato = testoCodificato.lower()
        testoCodificato = list(testoCodificato)
        alfabeto = "abcdefghijklmnopqrstuvwxyz"
        alfabeto = list(alfabeto)
        testovecchio = []
        for lettera in testoCodificato:
            if lettera in alfabeto:
                posizione = alfabeto.index(lettera)
                nuovaposizione = posizione-self.chiave
                if nuovaposizione>=0:
                    testovecchio.append(alfabeto[nuovaposizione])
                else:
                    nuovaposizione=nuovaposizione+len(alfabeto)
                    testovecchio.append(alfabeto[nuovaposizione])
        return testovecchio

class CifratoreACombinazione(CodificatoreMessaggio):
    def __init__(self,numero: int):
        self.numero = numero

    def codifica(self, testoInChiaro: str):
        testoInChiaro = testoInChiaro.lower()
        i = 0
        while i <= self.numero:
            if len(testoInChiaro) % 2!= 0:
                lunglistacorta = len(testoInChiaro) // 2
                lunglistalunga = lunglistacorta+1
                stringalunga = ''
                stringacorta = ''
                for n in range(0,lunglistalunga):
                    stringalunga += testoInChiaro[n]
                
                for i in range(lunglistalunga,len(testoInChiaro)):
                    stringacorta += testoInChiaro[n]
                
                testocambiato = ""
        i = i+1


        return testocambiato

        

# cifratore1 = CifratoreAScorrimento(3)
# print(cifratore1.codifica("ciaoz"))
# print(cifratore1.decodifica("fldrc"))

cifratore2 = CifratoreACombinazione(5)
print(cifratore2.codifica("Ciao"))




