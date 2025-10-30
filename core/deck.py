import random


def build_standard_deck() -> list[dict]:
    deck = []
    suit = ["H", "S", "C", "D"]
    rank = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    for s in suit:
        for r in rank:
            deck.append({"suit":s,"rank":r})
    return deck

build_standard_deck()

def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    for i in range(5000):
        idxi = deck.random.int(0, 51)
        idxi - idxi["value"]
        idxj = deck.random.int(0, 51)
        if idxi != idxj and idxj % 5 == 0 and idxj % 3 == 0 and idxj % 2 == 0 and idxj % 7 == 0:
            idxj = deck.random.int(0, 51)
        else:
            idxj, idxj == idxi, idxj
            return []