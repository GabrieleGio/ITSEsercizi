import random
percorso = ["-"] * 70
tartaruga = "T"
lepre = "H"
print("BANG !!!!! AND THEY'RE OFF !!!!!")
numero_random = random.randint(1,10)
print(percorso)

def calcola_tartaruga(percorso:list):
    numero_random = random.randint(1,10)
    if tartaruga not in percorso:
        #Passo veloce
        if 1 <= numero_random <= 5:
            percorso.pop(3)
            percorso.insert(3, tartaruga)
        
        #Scivolata
        elif 6 <= numero_random <= 7:
            percorso.pop(0)
            percorso.insert(0,tartaruga)
        
        #Passo lento
        elif 8 <= numero_random <= 10:
            percorso.pop(1)
            percorso.insert(1,tartaruga)
    else:
        #Passo veloce
        if 1 <= numero_random <= 5:
            nuovoindice = percorso.index(tartaruga) + 3
            percorso.pop(percorso.index(tartaruga))
            percorso.insert(percorso.index(tartaruga),"-")
            percorso.pop(nuovoindice)
            percorso.insert(nuovoindice,tartaruga)
        
        #Scivolata
        elif 6 <= numero_random <= 7:
            if percorso.index(tartaruga) - 6 < 0:
                percorso.pop(percorso.index(tartaruga))
                percorso.insert(percorso.index(tartaruga),"-")
                percorso.pop(0)
                percorso.insert(0,tartaruga)
            else:
                nuovoindice = percorso.index(tartaruga) - 6
                percorso.pop(percorso.index(tartaruga))
                percorso.insert(percorso.index(tartaruga),"-")
                percorso.pop(nuovoindice)
                percorso.insert(nuovoindice,tartaruga)
        
        #Passo lento
        elif 8 <= numero_random <= 10:
            nuovoindice = percorso.index(tartaruga) + 1
            percorso.pop(percorso.index(tartaruga))
            percorso.insert(percorso.index(tartaruga),"-")
            percorso.pop(nuovoindice)
            percorso.insert(nuovoindice,tartaruga)
    return percorso

print("#########################################")
print(len(percorso))
calcola_tartaruga(percorso)
print(percorso)
print(len(percorso))