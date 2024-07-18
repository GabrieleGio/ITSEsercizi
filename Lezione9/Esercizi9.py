import random
# Data una stringa s e una lista di stringhe wordDict, restituisce True se s può essere segmentato
# in una sequenza separata da spazi di una o più parole del dizionario; False altrimenti.
# Tieni presente che la stessa parola nel dizionario può essere riutilizzata più volte nella segmentazione.



###################################################################################################################################################

# Date due stringhe s e t, restituire True se t è un anagramma di s, e False altrimenti.
# Un anagramma è una parola o una frase formata riorganizzando le lettere di una parola o frase diversa, 
# in genere utilizzando tutte le lettere originali esattamente una volta.
"""
def anagramma(s:str, t:str) -> bool:
    s = s.lower()
    t = t.lower()

    if len(s) != len(t):
        return False,"Una delle due stringhe è più lunga dell'altra"
    
    paroleS = list(s)
    paroleT = list(t)

    parole2S = []
    parole2T = []

    for lettera in s:
        if lettera in t:
            parole2S.append(lettera)
            parole2T.append(lettera)
    
    if parole2S == parole2T and len(parole2T) == len(paroleT) and len(parole2S) == len(paroleS):
        return True,parole2S,parole2T
    else:
        return False, parole2S,parole2T

print(anagramma("anagram","nagaram"))
print(anagramma("rat", "car"))
print(anagramma("silent","listen"))
print(anagramma("NeurIPS","UniReps"))
"""





###################################################################################################################################################

# Progettare un semplice sistema bancario con i seguenti requisiti:

#     Classe del Account:
#         Attributi:
#             account_id: str - identificatore univoco per l'account.
#             balance: float - il saldo attuale del conto.
#         Metodi:
#             deposit(amount: float) - aggiunge l'importo specificato al saldo del conto.
#             get_balance(): restituisce il saldo corrente del conto.
#     Classe Bank:
#         Attributi:
#             accounts: dict[str, Account] - un dizionario per memorizzare gli account in base ai loro ID.
#         Metodi:
#             create_account(account_id): crea un nuovo account con l'ID specificato e un saldo pari a 0.
#             deposit(account_id, amount): deposita l'importo specificato sul conto con l'ID fornito.
#             get_balance(account_id): restituisce il saldo del conto con l'ID specificato.
account_usati = []
alfabeto = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
account_id = alfabeto[random.randint(0,25)] + str(random.randint(1,9999))
while account_id in account_usati:
        account_id = alfabeto[random.randint(0,25)] + str(random.randint(1,9999))

print(account_id)
print(account_usati)
class Account:
    def __init__(self) -> None:
        self.account_id = alfabeto[random.randint(0,25)] + str(random.randint(1,9999))
        while self.account_id in account_usati:
            self.account_id = alfabeto[random.randint(0,25)] + str(random.randint(1,9999))
            

        pass
