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