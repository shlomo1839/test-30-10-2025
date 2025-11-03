from deck import build_standard_deck, deck
import random

def calculate_hand_value(hand: list[dict]) -> int:
    deck = {"1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q": 10, "K": 10}
    for r in ["rank"]:
        sum += r
        return sum
    

def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    card_player1 = deck.pop()
    player["hand"].append(card_player1)
    card_player2 = deck.pop()
    player["hand"].append(card_player2)
    print("hand player: card_player1, card_player2")

    card_deler1 = deck.pop()
    dealer["hand"].append(card_deler1)
    card_dealer2 = deck.pop()
    dealer["hand"].append(card_dealer2)
    print("hand dealer: card_dealer1, card_dealer2")
    return

def dealer_play(deck: list[dict], dealer: dict) -> bool:
    while sum < 17:
        temp = deck.pop()
        sum += temp
        if sum > 17:
            return True
        else:
            return False

def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    pass