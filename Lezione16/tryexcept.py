#Qua c'è un esempio di come funziona il try e except

try:
    print("Sono nmel try")
    #Per lanciare un eccezione:
    raise ValueError()

#Nell'except puoi specificare il tipo di eccezione
except ValueError:
    print("Sono nel Value Error")

except ZeroDivisionError:
    print("Sono nello ZeroDivision Error")

except ImportError:
    print("Sono nell'Import Error")


else:
    print("Sono nell'else")

finally:
    print("Sono nel finally")
