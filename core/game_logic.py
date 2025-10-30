from deck import build_standard_deck, deck
import random

def calculate_hand_value(hand: list[dict]) -> int:
    values = {"1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q": 10, "K": 10}
    for h in ["hand"]:
        sum += h
        return sum
    

def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    card_player1 = deck.pop()
    player["hand"] += card_player1
    print("your card is" + card_player1)
    card_player2 = deck.pop()
    player["hand"] += card_player2
    print("your card is" + card_player2)
    card_deler1 = deck.pop()
    dealer["hand"] += card_deler1
    print("your card is" + card_deler1)
    card_dealer2 = deck.pop()
    dealer["hand"] += card_dealer2
    print("your card is" + card_dealer2)
    return deck
    
    

def dealer_play(deck: list[dict], dealer: dict) -> bool:
    while True:
        temp = deck.pop()
        deck["hand_dealer"] += temp
        if deck["hand_dealer"] > 21:
            print("The dealer lost")
            return False
        else:
            if deck["hand_dealer"] >= 17:
                print("The delir has finished the turn. Your turn")
                return True

def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    pass