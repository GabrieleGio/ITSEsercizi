#Qua c'è un esempio di come funziona il try e except

#Posso anche creare eccezioni personalizzate
class ErrorePersonalizzato(Exception):
    pass

try:
    print("Sono nel try")
    #Per lanciare un eccezione:
    #raise ValueError
    raise ErrorePersonalizzato()

#Nell'except puoi specificare il tipo di eccezione
except ValueError:
    print("Sono nel Value Error")

except ZeroDivisionError:
    print("Sono nello ZeroDivision Error")

except ImportError:
    print("Sono nell'Import Error")

except ErrorePersonalizzato:
    print("Sono nell'errore personalizzato")

else:
    print("Sono nell'else")

finally:
    print("Sono nel finally")

