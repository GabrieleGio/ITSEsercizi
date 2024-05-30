import random

def visualizza_posizioni(pos_tartaruga, pos_lepre):
    percorso = ['-'] * 70
    percorso[pos_tartaruga - 1] = 'T'
    percorso[pos_lepre - 1] = 'H'
    if pos_tartaruga == pos_lepre and pos_tartaruga != 1:
        percorso[pos_tartaruga - 1] = 'OUCH!!!'
    elif pos_tartaruga == pos_lepre and pos_tartaruga == 1:
        percorso[pos_tartaruga - 1] = 'T and H'
    print(percorso)


def muovi_tartaruga():
    i = random.randint(1, 10)
    #Passo veloce
    if 1 <= i <= 5:
        return 3
    #Scivolata
    elif 6 <= i <= 7:
        return -6
    #Passo lento
    else:
        return 1


def muovi_lepre():
    i = random.randint(1, 10)
    if i == 1:
        return 9
    elif 2 <= i <= 3:
        return -12
    elif 4 <= i <= 6:
        return 1
    else:
        return -2


pos_tartaruga = 1
pos_lepre = 1
tick = 0
tickpioggia = 0
cambiamentometeo = False
meteo = "Sereno"
print("BANG !!!!! AND THEY'RE OFF !!!!!")

while pos_tartaruga < 70 and pos_lepre < 70:

    #Controllo meteo
    if meteo == "Pioggia" and tickpioggia == 10:
        meteo = "Sereno"
        print("!!! NOW IT'S SUNNY !!!")
        cambiamentometeo = True
        tickpioggia = 0


    #Inizio pioggia
    if tick % 10 == 0 and tick != 0 and cambiamentometeo == False:
        meteo = "Pioggia"
        print("!!! IT'S RAINING !!!")
    
    #Gestione durata della pioggia
    if meteo == "Pioggia":
        tickpioggia += 1
    

    mosse = {'tartaruga': muovi_tartaruga(), 'lepre': muovi_lepre()}
    #Muovo la tartaruga e la lepre

    #Penalità per la pioggia tartaruga
    if meteo == "Pioggia":
        pos_tartaruga += (mosse['tartaruga'] - 1)
    else:
        pos_tartaruga += mosse['tartaruga']

    if pos_tartaruga < 1:
        pos_tartaruga = 1
    
    #Penalità per la pioggia lepre
    if meteo == "Pioggia":
        pos_lepre += (mosse['lepre'] - 2)
    else:
        pos_lepre += mosse['lepre']

    if pos_lepre < 1:
        pos_lepre = 1
    
    #Uscite dalla gara
    if pos_tartaruga >= 70: 
        print("TORTOISE WINS! || VAY!!!")
        break

    if pos_lepre >= 70:
        print("HARE WINS || YUCH!!!")
        break

    if pos_lepre == pos_tartaruga and pos_tartaruga == 70:
        print("IT'S A TIE.")
        break
    
    #Stampo le posizioni e aumento il tempo
    visualizza_posizioni(pos_tartaruga, pos_lepre)
    tick += 1
    cambiamentometeo = False
    print(tick)

    #Vedere quando disattivare cambiamento meteo True
    