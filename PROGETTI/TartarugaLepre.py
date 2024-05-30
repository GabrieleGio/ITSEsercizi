import random


def visualizza_posizioni(pos_tartaruga, pos_lepre):
    percorso = ['-'] * 70
    percorso[pos_tartaruga - 1] = 'T'
    percorso[pos_lepre - 1] = 'H'
    if pos_tartaruga == pos_lepre:
        percorso[pos_tartaruga - 1] = 'OUCH!!!'
    print(percorso)


def muovi_tartaruga():
    i = random.randint(1, 10)
    if 1 <= i <= 5:
        return 3
    elif 6 <= i <= 7:
        return -6
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


print("BANG !!!!! AND THEY'RE OFF !!!!!")

while pos_tartaruga < 70 and pos_lepre < 70:

    mosse = {'tartaruga': muovi_tartaruga(), 'lepre': muovi_lepre()}
    

    pos_tartaruga += mosse['tartaruga']
    if pos_tartaruga < 1:
        pos_tartaruga = 1
    pos_lepre += mosse['lepre']
    if pos_lepre < 1:
        pos_lepre = 1
    
    if pos_tartaruga >= 70: 
        print("TORTOISE WINS! || VAY!!!")
        break

    if pos_lepre >= 70:
        print("HARE WINS || YUCH!!!")
        break

    if pos_lepre == pos_tartaruga and pos_tartaruga == 70:
        print("IT'S A TIE.")
        break
    
    visualizza_posizioni(pos_tartaruga, pos_lepre)