def ask_player_action() -> str:
    request = input("do you want to play? enter H to playת or S If you don't want to play")
    if request != "S" or request != "H":
        print("invalid char, please enter again")
    elif request == "S":
        return "S"
    else:
        return "H"
    
    
    
print(ask_player_action("S"))
