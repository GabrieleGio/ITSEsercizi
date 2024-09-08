#Esercizio 1
def frequency_dict(elements: list) -> dict:
    diz = {}
    for element in elements:
        if element not in diz.keys():
            diz[element] = 1
        else:
            diz[element] += 1
    return diz

lista = ["mela","pera","banana","banana","cocomero","mela"]
print(frequency_dict(lista))



def sum_above_threshold(numbers: list[int], threshold: int) -> int:
    somma = 0
    for number in numbers:
        if number > threshold:
            somma = somma + number
    return somma


def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
    newdict = {}
    for k,v in prodotti.items():
        if prodotti[k] > 20:
            newdict[k] = prodotti[k] - prodotti[k]*(1/10)
    return newdict


#Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori.
def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    for k,v in dict2.items():
        if k not in dict1.keys():
            dict1[k] = v
        else:
            dict1[k] += v
    return dict1


def lista_a_dizionario(tuples: list[tuple]) -> dict[str:list[int]]:
    newdict = {}
    for tupla in tuples:
        if tupla[0] not in newdict.keys():
            newdict[tupla[0]] = [tupla[1]]
        else:
            newdict[tupla[0]] += [tupla[1]]
    return newdict

lista1 = [("ciao","marco"),(20,"sium")]
lista_a_dizionario(lista1)

#Scrivi una funzione che prenda un dizionario e un valore, e ritorni la prima chiave che corrisponde a quel valore, o None se il valore non è presente.
def trova_chiave_per_valore(dizionario: dict[str: int], valore: int) -> str:
    for k,v in dizionario.items():  
        if dizionario[k] == valore:
            return v
