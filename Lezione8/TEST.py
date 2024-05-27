def longest_palindrome(s: str) -> int:
    diz = {}
    lista = []
    for lettera in s:
        diz[lettera] = s.count(lettera)
    
    #while diz == None:
    for key,values in diz.items():
        if values > 1:
            for i in range(0,values//2):
                lista.append(key)
                lista.insert(0,key)
                diz[key]-=2

    for key,values in diz.items():
        if values!=0:
            lista.insert((len(lista)//2,key))
            return len(lista)
    return len(lista)

        