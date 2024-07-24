#Paradosso di Monty Hall
import random

numeri_casuali = random.sample(range(1,4), 3)
porta1,porta2,porta3 = numeri_casuali
if porta1 == 1:
    portagiusta = porta1
    portasbagliata1 = porta2
    portasbagliata2 = porta3
if porta2 == 1:
    portagiusta = porta2
    portasbagliata1 = porta1
    portasbagliata2 = porta3
if porta3 == 1:
    portagiusta = porta3
    portasbagliata1 = porta1
    portasbagliata2 = porta2


while True:
    scelta = input("Scegli tra porta1, porta2 o porta3: ").lower()
    if scelta == "porta1":
        scelta = porta1
        break
    elif scelta == "porta2":
        scelta = porta2
        break
    elif scelta == "porta3":
        scelta = porta3
        break
    else:
        print("Scelta non valida, devi inserire porta1, porta2 o porta3")

if scelta == portagiusta:
    cambio = input(f"La porta {portasbagliata1} è sbagliata, vuoi cambiare la tua scelta? (si/no) ")
    if cambio == "si":
        nuovascelta = portasbagliata2
    if cambio == "no":
        print("Hai vinto!")

if scelta == portasbagliata1:
    cambio = input(f"La porta {portasbagliata2} è sbagliata, vuoi cambiare la tua scelta? (si/no) ")
    if cambio == "si":
        nuovascelta = portagiusta
    if cambio == "no":
        print("Hai perso")
        

if scelta == portasbagliata2:
    cambio = input(f"La porta {portasbagliata1} è sbagliata, vuoi cambiare la tua scelta? (si/no) ")
    if cambio == "si":
        nuovascelta = portasbagliata1
    if cambio == "no":
        print("Hai perso")
        


