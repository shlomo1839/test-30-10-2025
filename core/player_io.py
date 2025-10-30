
from coor.deck import run_full_game
def ask_player_action() -> str:
    request = input("do you want to play?")
    if request.isalpha():
        if request is not "H" or "S":
            print("Your answer is incorrect. Do you want to play?")
    elif request == "S":
        print("end game")
    else:
        run_full_game()


    return ""

