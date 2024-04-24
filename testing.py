def blackjack_hand_total(cards: list[int]) -> int:
    valore = 0
    asso = 0
    if 11 in cards and sum(cards) > 21:
        asso = cards.index(11)
        cards[asso] = 1
        valore = sum(cards)
    else:
        valore = sum(cards)
    return valore
print()
####################################################
def find_lhs(nums: list[int]) -> int:
    for n in range(len(nums)):
        for n in range(len(nums)):
            return n

print(find_lhs([1,3,2,2,5,2,3,7]))