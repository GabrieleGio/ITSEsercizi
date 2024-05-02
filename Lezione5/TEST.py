#Scrivi una funzione che verifica se una combinazione di condizioni (A, B, e C) è soddisfatta per procedere con un'operazione. 
#L'operazione può procedere solo se la condizione A è vera o se entrambe le condizioni B e C sono vere. 
#La funzione deve ritornare "Operazione permessa" oppure "Operazione negata" a seconda delle condizioni che sono soddisfatte.
def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
    if conditionA == True:
        return "Operazione permessa"
    elif conditionB == True and conditionC == True:
        return "Operazione permessa"
    else:
        return "Operazione negata"
    
print()
print()

#Scrivi una funzione che ritorna il valore massimo, minimo e la media di una lista di numeri interi.
def list_statistics(numbers: list[int]) -> int :
    somma=0
    media=0
    for n in numbers:
        somma = somma + n
    media = somma / len(numbers)
    return max(numbers),min(numbers),media

print()
print()

#Scrivi una funzione che, data una lista, ritorni un dictionary che mappa ogni elemento alla sua frequenza nella lista.
def frequency_dict(elements: list) -> dict:
    diz = {}
    for n in elements:
        diz[n] = elements.count(n)
    return diz

list = ["mela","banana","mela"]

print(frequency_dict(list))

print()
print()

#Scrivi una funzione che accetti tre parametri: username, password e status di attivazione dell'account (attivo/non attivo). 
#L'accesso è consentito solo se il nome utente è "admin", la password corrisponde a "12345" e l'account è attivo. 
#La funzione ritorna "Accesso consentito" oppure "Accesso negato".
def check_access(username: str, password: ..., is_active: bool) -> str:
    if username == "admin" and password == "12345" and is_active == True:
        return "Accesso consentito"
    else:
        return "Accesso negato"
    
print()
print()

#La funzione dovrebbe calcolare la media dei numeri in una lista di interi.
#Un errore nell'implementazione porta a risultati inaspettati.
def calculate_average(numbers: list[int]) -> float:
    if len(numbers) != 0:
        return sum(numbers) / len(numbers)
    else:
        return 0
print()
print()

#Scrivi una funzione che rimuove tutti i duplicati da una lista, contenente sia numeri che lettere, mantenendo l'ordine originale degli elementi.
def remove_duplicates(lista: list) -> list:
    lista2 = []
    for k in lista:
        if k not in lista2:
            lista2.append(k)
    return lista2

print()
print()

#Scrivi una funzione che verifica se in una stringa le parentesi '(' e ')' sono bilanciate, cioè per ogni 
#parentesi che apre c'è la corrispondente parentesi che chiude.
def check_parentheses(expression: str) -> bool:
    c = 0
    for k in expression:
        if k == "(":
            c = c+1
        if k == ")":
            c = c-1
        if c < 0:
            return False
    if c == 0:
        return True
    else:
        return False
        
        


print(check_parentheses("()()"))
print(check_parentheses("(()))("))

print()
print()

#Scrivi una funzione che conta e ritorna quante volte un elemento appare isolato in una lista di numeri interi. 
#Un elemento è considerato isolato se non è affiancato sia a destra che a sinistra da elementi uguali.
def count_isolated(lista: list) -> int:
    isolati = 0
    if lista == []:
        return 0
    for n in range(1,len(lista)-1):
        if lista[n] != lista[n-1] and lista[n] != lista[n+1]:
            isolati = isolati + 1
    if lista[0] != lista[1]:
        isolati = isolati + 1
    if lista[-1] != lista[-2]:
        isolati = isolati + 1
    return isolati

print(count_isolated([1, 2, 2, 3, 3, 3, 4]))
print(count_isolated([1, 2, 3, 4, 5]))

print()
print()

#Scrivi una funzione che, dato un insieme e una lista di numeri interi da rimuovere, ritorni un nuovo insieme senza i numeri specificati nella lista.
def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
    for k in elements_to_remove:
        if k in original_set:
            original_set.remove(k)
    return original_set

print()
print()

#Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori.
def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()

    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value
    return merged_dict

print()
print()