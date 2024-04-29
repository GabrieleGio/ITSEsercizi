def find_disappeared_numbers(nums: list[int]) -> list[int]:
    l: list = []
    l_mancanti: list = []
    for n in range(min(nums),len(nums)+1):
        l.append(n)
    for n in l:
        if n not in nums:
          l_mancanti.append(n)
    return l_mancanti

print(find_disappeared_numbers([4,3,2,7,8,2,3,1]))

####################################################################
def somma_elementi(x: list[int], y: list[int]) -> list[int]:
    listanuova = []
    listapiupiccola = []
    if len(x) > len(y):
        listapiupiccola = y
    elif len(x) < len(y):
        listapiupiccola = x
    else:
        listapiupiccola = x
    for n in range(len(listapiupiccola)):
       listanuova.append(x[n] + y[n])
    return listanuova

print(somma_elementi([1,1,1],[1,1,1]))
print(somma_elementi([-10,-2],[10]))

print()
#########################################################################

#############################
def prime_factors(n: int) -> list[int]:

    primi = []

    i = 2

    while i * i <= n:

        if n % i:

            i += 1

        else:

            n //= i

            primi.append(i)

    if n > 1:

        primi.append(n)

    return primi
print(prime_factors(4))
print(prime_factors(60))
print(prime_factors(627))
print(prime_factors(622919))
print(prime_factors(999999999999999999))
########################################################
def third_max(nums: list[int]) -> int:
    nums = set(nums)
    massimo = 0
    if len(nums) >= 3:
        massimo = max(nums)-2
    else:
        massimo = max(nums)
    return massimo
print(third_max([3, 2, 1]))
print(third_max([1, 2]))
print()
print()
#####################################################
def even_odd_pattern(nums: list[int]) -> list[int]:
    lnuova = []
    lnuova2 = []
    lnuova3 = []
    for n in nums:
        if n % 2 == 0:
            lnuova.append(n)
        elif n % 2 != 0:
            lnuova2.append(n)
    lnuova3 = lnuova + lnuova2
    return lnuova3
print(even_odd_pattern([3, 6, 1, 8, 4, 7]))
#usando insert e append sarebbe stato più efficiente

####################################################################
def blackjack_hand_total(cards: list[int]) -> int:
    valore = 0
    asso = 0
    if 1 in cards and sum(cards) <= 10:
        asso = cards.index(1)
        cards[asso] = 11
        valore = sum(cards)
    else:
        valore = sum(cards)
    return valore
print(blackjack_hand_total([2, 3, 5]))
#risulato 10
