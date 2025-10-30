from core.deck import build_standard_deck, shuffle_by_suit





if __name__ == "__main__":
    
    deck = build_standard_deck()

    deck_suffle = shuffle_by_suit(deck)

    player = {"hand": [ ] }
    dealer = {"hand": [ ] }
