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
        idxi = random.randint(0, 51)
        idxi - idxi["value"]
        idxj = random.randint(0, 51)
        idxj - idxj["value"]

        if idxi["value"] != idxj["value"]:
            if idxj["suit"] == "H":
                if idxj % 5 != 0:
                    idxj = random.randint(0, 51)
            if idxj["suit"] == "C":
                if idxj % 3 != 0:
                    idxj = random.randint(0, 51)
            if idxj["suit"] == "D":
                if idxj % 2 != 0:
                    idxj = random.randint(0, 51)
            if idxj["suit"] == "S":
                if idxj % 7 != 0:
                    idxj = random.randint(0, 51)
            idxi, idxj == idxj, idxi
            return [deck]