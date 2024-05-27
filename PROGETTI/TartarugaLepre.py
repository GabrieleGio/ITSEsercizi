import random
percorso = ["-"] * 70
tartaruga = "T"
lepre = "H"
print("BANG !!!!! AND THEY'RE OFF !!!!!")
numero_random = random.randint(1,10)
print(percorso)

def calcola_tartaruga(percorso:list):
    numero_random = random.randint(1,10)

    #Passo veloce
    if 1 <= numero_random <= 5:
       nuovoindice = percorso.index(tartaruga) + 3
       percorso.pop(tartaruga)
       percorso.insert(nuovoindice,tartaruga)
    
    #Scivolata
    elif 6 <= numero_random <= 7:
        if percorso.index(tartaruga) - 6 < 0:
            percorso.pop(tartaruga)
            percorso.insert(0,tartaruga)
        else:
            nuovoindice = percorso.index(tartaruga) - 6
            percorso.pop(tartaruga)
            percorso.insert(nuovoindice,tartaruga)
    
    #Passo lento
    elif 8 <= numero_random <= 10:
       nuovoindice = percorso.index(tartaruga) + 1
       percorso.pop(tartaruga)
       percorso.insert(nuovoindice,tartaruga)
    return percorso



while True:
