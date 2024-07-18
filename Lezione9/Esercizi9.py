# Data una stringa s e una lista di stringhe wordDict, restituisce True se s può essere segmentato
# in una sequenza separata da spazi di una o più parole del dizionario; False altrimenti.
# Tieni presente che la stessa parola nel dizionario può essere riutilizzata più volte nella segmentazione.

###################################################################################################################################################

# Date due stringhe s e t, restituire True se t è un anagramma di s, e False altrimenti.
# Un anagramma è una parola o una frase formata riorganizzando le lettere di una parola o frase diversa, 
# in genere utilizzando tutte le lettere originali esattamente una volta.

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
