def substract_all(x: list[float], y: float) -> list[float]:
    # x = [1,2,3,4,5]
    # y = 5
    # restituisce [-4,-3,-2,-1,0]
    l=[]
    for n in x:
        l.append(n-y)
    return l
lista = [1,2,3,4,5]
print(substract_all(lista,5))

print()
print()


def add_diff_to_res(x: list[float], y: list[float], lenght: int) -> list[float]:
    res: list[float] = []
    for i in range(lenght):
        diff = x[i] - y[i]
        res.append(diff)
    return res

def substract_all2(x: list[float], y: float) -> list[float]:
    lenght = min(len(x), len(y))
    res: list[float] = add_diff_to_res(x,y,lenght)
    return res

lista = [1,2,3,4,5]
lista2 = [2,3,4,5,6]
print(substract_all2(lista,lista2))

s = "La meccanica quantistica è la teoria fisica che descrive il comportamento della materia, della radiazione e le reciproche interazioni, con particolare riguardo ai fenomeni caratteristici della scala di lunghezza o di energia atomica e subatomica, dove le precedenti teorie classiche risultano inadeguate. Come caratteristica fondamentale, la meccanica quantistica descrive la radiazione e la materia sia come fenomeni ondulatori che come entità particellari, al contrario della meccanica classica, che descrive la luce solamente come un'onda e, ad esempio, l'elettrone solo come una particella. Questa inaspettata e controintuitiva proprietà della realtà fisica, chiamata dualismo onda-particella, è la principale ragione del fallimento delle teorie sviluppate fino al XIX secolo nella descrizione degli atomi e delle molecole. La relazione tra natura ondulatoria e corpuscolare è enunciata nel principio di complementarità e formalizzata nel principio di indeterminazione di Heisenberg. Esistono numerosi formalismi ma"
def counter(s: str) -> list[int]:
    """
    Questa funzione prende una stringa in input e
    restituisce una lista costruita nel modo seguente:
    - il primo elemento della lista contiene il numero di caratteri nella stringa
    - il secondo elemento della lista contiene il numero di parole nella stringa
    - il terzo elemento della lista contiene il numero di parole distinte nella stringa
    - il quarto elemento della lista contiene il numero di frasi nella stringa
    """
    primo = len(s)
    secondo = len(s.split())
    terzo = len(set(s.split()))
    quarto = len(s.split("."))
    return [primo,secondo,terzo,quarto]
print(counter(s))

def word_count(s: str) -> dict[str, int]:
    """
    Questa funzione conta il numero di occorrenza delle parole di una stringa
    es: se la stringa è "ciao come stai. tutto bene. ciao io sto bene"
    il risultato deve essere
    {"ciao": 2, "come": 1, "stai" : 1, "tutto" : 1, "bene" : 2, "io" : 1, "sto" : 1}
    """
    parole: list[str] = s.split()
    d: dict[str,int] = dict()
    for parola in parole:
        if parola not in d:
            d[parola] = 1
        else:
            d[parola] = d[parola] + 1
#filtra soltanto le parole che compaiono > 1 volta
    d_filtered: dict[str, int] = dict()
    for key in d:
        if d[key] > 1:
            d_filtered[key] = d[key]
    return d_filtered

s1 = "ciao come stai. tutto bene. ciao io sto bene"
print(word_count(s1))

print()
print()

def is_palindromo(s: str) -> bool:
    """
    Restituisce True se s è palindroma, altrimenti restituisce False
    e.s. "Amo Roma" è una stringa palindroma
    e.s. "ciao come stai?" non è una stringa palindroma
    """
    palindroma = bool
    s: str = s.lower().replace(' ', '')
    q = 0
    p = -1
    for l in s:
        if s[q] == s[p]:
            palindroma = True
            q = q + 1
            p = p - 1
        else:
            palindroma = False
    return palindroma

frase = "Amo Roma"
print(is_palindromo(frase))
frase1 = "Ciao come stai?"
print(is_palindromo(frase1))
frase3 = "I topi non avevano nipoti"
print(is_palindromo(frase3))
