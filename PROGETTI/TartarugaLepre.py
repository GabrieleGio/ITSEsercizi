import random

# Definizione della funzione per visualizzare le posizioni sulla corsia di gara
def visualizza_posizioni(pos_tartaruga, pos_lepre):
    percorso = ['-'] * 70
    percorso[pos_tartaruga - 1] = 'T'
    percorso[pos_lepre - 1] = 'H'
    if pos_tartaruga == pos_lepre:
        percorso[pos_tartaruga - 1] = 'OUCH!!!'
    print(''.join(percorso))

# Definizione della funzione per calcolare la mossa della tartaruga
def muovi_tartaruga():
    i = random.randint(1, 10)
    if 1 <= i <= 5:
        return 3
    elif 6 <= i <= 7:
        return -6
    else:
        return 1

# Definizione della funzione per calcolare la mossa della lepre
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

# Impostazione delle posizioni iniziali
pos_tartaruga = 1
pos_lepre = 1

# Stampa dell'inizio della gara
print("BANG !!!!! AND THEY'RE OFF !!!!!")

# Simulazione dei ticks dell'orologio
while pos_tartaruga <= 70 and pos_lepre <= 70:
    # Calcolo delle mosse
    mosse = {'tartaruga': muovi_tartaruga(), 'lepre': muovi_lepre()}
    
    # Aggiornamento delle posizioni
    pos_tartaruga += mosse['tartaruga']
    if pos_tartaruga < 1:
        pos_tartaruga = 1
    pos_lepre += mosse['lepre']
    if pos_lepre < 1:
        pos_lepre = 1
    
    # Visualizzazione delle posizioni
    visualizza_posizioni(pos_tartaruga, pos_lepre)

# Stampa del risultato
if pos_tartaruga == pos_lepre:
    print("IT'S A TIE.")
elif pos_tartaruga > pos_lepre:
    print("TORTOISE WINS! || VAY!!!")
else:
    print("HARE WINS || YUCH!!!")