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

# account_usati = []
# alfabeto = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
# def generatore_account_unico():
#     while True:
#         account_id = alfabeto[random.randint(0,25)] + str(random.randint(1,9999))
#         if account_id not in account_usati:
#             account_usati.append(account_id)
#             return account_id

class Account:
    def __init__(self,account_id,balance) -> None:
        self.account_id: str = account_id
        self.balance: float = balance
    
    def deposit(self,amount: float):
        self.amount = amount
        self.balance = self.balance + self.amount

    def get_balance(self):
        return self.balance
    
    def __str__(self):
        return self.account_id,self.balance
    
class Bank:
    def __init__(self) -> None:
        self.accounts: dict[str,Account] = {}

    def create_account(self,account_id):
        self.account = Account(account_id,0)
        if account_id not in self.accounts.keys():
            self.accounts[account_id] = self.account
        else:
            print("Errore, l'account esiste già")
        return self.account
    
    def deposit(self,account_id, amount):
        if account_id in self.accounts.keys():
            self.accounts.balance += amount
        else:
            print(f"Errore, l'account {account_id} non esiste")

    def get_balance(self,account_id):
        if account_id in self.accounts:
            return self.accounts.balance
        else:
            print(f"Errore, l'account {account_id} non esiste")

    def __str__(self) -> str:
        
        return str(self.accounts)

bank1 = Bank()
bank1.create_account("B456")
print(bank1)
account1 = Account("A123","15")


        


    
