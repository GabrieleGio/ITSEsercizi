print()
l=[]
dizionario = {"Chiave1":"Valore1", "Chiave2":"Valore2", "Chiave3":"Valore3"}
print(dizionario)
print()

for chiave,valore in dizionario.items():
    print(chiave)
    print(valore)
    l.append(valore)
print(l)
