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
print(set(s.split()))