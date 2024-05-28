import random
percorso = ["-"] * 70
percorso_ouch = percorso
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
            indiceT = percorso.index(tartaruga)
            nuovoindice = percorso.index(tartaruga) + 3
            percorso.pop(indiceT)
            percorso.insert(indiceT,"-")
            percorso.pop(nuovoindice)
            percorso.insert(nuovoindice,tartaruga)
        
        #Scivolata
        elif 6 <= numero_random <= 7:
            if percorso.index(tartaruga) - 6 < 0:
                indiceT = percorso.index(tartaruga)
                percorso.pop(indiceT)
                percorso.insert(indiceT,"-")
                percorso.pop(0)
                percorso.insert(0,tartaruga)
            else:
                indiceT = percorso.index(tartaruga)
                nuovoindice = percorso.index(tartaruga) - 6
                percorso.pop(indiceT)
                percorso.insert(indiceT,"-")
                percorso.pop(nuovoindice)
                percorso.insert(nuovoindice,tartaruga)
        
        #Passo lento
        elif 8 <= numero_random <= 10:
            indiceT = percorso.index(tartaruga)
            nuovoindice = percorso.index(tartaruga) + 1
            percorso.pop(indiceT)
            percorso.insert(indiceT,"-")
            percorso.pop(nuovoindice)
            percorso.insert(nuovoindice,tartaruga)

    return percorso

def calcola_lepre(percorso: list):
    """
    - Riposo (20% di probabilità): non si muove.
    - Grande balzo (20% di probabilità): avanza di 9 quadrati.
    - Grande scivolata (10% di probabilità): arretra di 12 quadrati. Non può andare sotto il quadrato 1.
    -  Piccolo balzo (30% di probabilità): avanza di 1 quadrato.
    - Piccola scivolata (20% di probabilità): arretra di 2 quadrati. Non può andare sotto il quadrato 1.
    """
    numero_random2 = random.randint(1,10)
    if lepre not in percorso:
        #Riposo
        if 1 <= numero_random2 <= 2:
            percorso.pop(0)
            percorso.insert(0,lepre)
        
        #Grande balzo
        elif 3 <= numero_random2 <= 4:
            percorso.pop(9)
            percorso.insert(9,lepre)
        
        #Grande scivolata
        elif numero_random2 == 5:
            percorso.pop(0)
            percorso.insert(0,tartaruga)

        #Piccolo balzo
        elif 6 <= numero_random2 <= 8:
            percorso.pop(1)
            percorso.insert(1,lepre)
        
        #Piccola scivolata
        elif 9 <= numero_random2 <= 10:
            percorso.pop(0)
            percorso.insert(0,lepre)

    else:
        #Riposo
        if 1 <= numero_random2 <= 2:
            indiceL = percorso.index(lepre)
            percorso.pop(indiceL)
            percorso.insert(indiceL,lepre)
        
        #Grande balzo
        elif 3 <= numero_random2 <= 4:
            indiceL = percorso.index(lepre)
            nuovoindice2 = percorso.index(lepre) + 9
            percorso.pop(indiceL)
            percorso.insert(indiceL,"-")
            percorso.pop(nuovoindice2)
            percorso.insert(nuovoindice2,lepre)
        
        #Grande scivolata
        elif numero_random2 == 5:
            if percorso.index(tartaruga) - 12 < 0:
                indiceT = percorso.index(tartaruga)
                percorso.pop(indiceT)
                percorso.insert(indiceT,"-")
                percorso.pop(0)
                percorso.insert(0,tartaruga)
            else:
                indiceL = percorso.index(lepre)
                nuovoindice2 = percorso.index(lepre) - 12
                percorso.pop(indiceL)
                percorso.insert(indiceL,"-")
                percorso.pop(nuovoindice2)
                percorso.insert(nuovoindice2,lepre)
        
        #Piccolo balzo
        elif 6 <= numero_random2 <= 8:
            indiceL = percorso.index(lepre)
            nuovoindice2 = percorso.index(lepre) + 1
            percorso.pop(indiceL)
            percorso.insert(indiceL,"-")
            percorso.pop(nuovoindice2)
            percorso.insert(nuovoindice2,lepre)
        
        #Piccola scivolata
        elif 9 <= numero_random2 <= 10:
            if percorso.index(tartaruga) - 2 < 0:
                indiceT = percorso.index(tartaruga)
                percorso.pop(indiceT)
                percorso.insert(indiceT,"-")
                percorso.pop(0)
                percorso.insert(0,tartaruga)
            else:
                indiceL = percorso.index(lepre)
                nuovoindice2 = percorso.index(lepre) - 2
                percorso.pop(indiceL)
                percorso.insert(indiceL,"-")
                percorso.pop(nuovoindice2)
                percorso.insert(nuovoindice2,lepre)
    return percorso

calcola_tartaruga(percorso)
calcola_lepre(percorso)


while True:
    calcola_tartaruga(percorso)
    indiceT = percorso.index(tartaruga)
    calcola_lepre(percorso)
    indiceL = percorso.index(lepre)
    if indiceL == indiceT:
        percorso.pop(indiceL)
        percorso.insert()

print("#########################################")
print(len(percorso))
calcola_tartaruga(percorso)
print(percorso)
print(len(percorso))
print("")
print("################ DI NUOVO ################")
print("")
calcola_tartaruga(percorso)
calcola_lepre(percorso)
print(percorso)
print(len(percorso))