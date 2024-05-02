def frequency_dict(elements: list) -> dict:
    diz = {}
    for n in elements:
        diz[n] = elements.count(n)
    return diz

list = ["mela","banana","mela"]

print(frequency_dict(list))

def remove_duplicates(lista: list) -> list:
    for k in lista:
        if lista.count(k) > 1:
            lista.remove(k)
    return lista

list2 = ["mela","banana","mela","pera","mango","mela","pera","banana","arancia"]


print()
print()
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

def count_isolated(lista: list) -> int:
    isolati = 0
    for n in range(1,len(lista)-1):
        if lista[n] != lista[n-1] and lista[n] != lista[n+1]:
            isolati = isolati + 1

print(count_isolated([1, 2, 2, 3, 3, 3, 4]))
print(count_isolated([1, 2, 3, 4, 5]))


def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()

    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value
    return merged_dict

