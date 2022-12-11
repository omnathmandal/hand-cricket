from .gamelogic import *
from colorama import Fore, Back, Style

def normal() -> None:
    print(Fore.LIGHTBLACK_EX + f"\n{'+'*50}")
    print(Fore.LIGHTMAGENTA_EX + "<<<<<<<<<<\t WELCOME \t>>>>>>>>>>")
    print(Fore.LIGHTBLACK_EX + f"{'+'*50}")
    # input for overs and number of players
    o = int(input(Fore.LIGHTGREEN_EX + "\nEnter the number of Overs :"))
    n = inputR2(2)
    # lists for Scorcard and player names
    pn = []
    bn = []
    pl = [0] * n
    b = [0] * n
    print(Fore.LIGHTBLACK_EX + f"\n{'~'*50}")
    print(Fore.YELLOW + "<--  Please enter the names of the players -->")
    print(Fore.LIGHTBLACK_EX + f"{'-'*50}\n")
    addPlayerName(n, pn)
    botname(n, bn)
    print(Fore.LIGHTBLACK_EX + f"\n{'^'*50}")
    batsman = matchStart()

    if batsman == "player":
        target = firstInn(o, pl, n, batsman)
        print(Fore.LIGHTRED_EX + f"Score :\t {target[0]}/{target[1]}")
        print(Fore.LIGHTBLACK_EX + "-" * 50)
        print(Fore.LIGHTRED_EX + f"\t<-- Target = {target[0]} -->")
        print(Fore.LIGHTBLACK_EX + "-" * 50)
        target2 = secondInn(o, b, n, "bot", target[0])
        print(Fore.LIGHTBLACK_EX + f"\n{'-'*50}")
        print(Fore.BLUE + "\t<<<<< SCOREBOARD >>>>>")
        print(Fore.LIGHTBLACK_EX + "-" * 50)
        print(Fore.LIGHTBLUE_EX + ">>>\tFirst Innings\t<<<\n")
        Scorcard(pn, pl, target[0], target[1])
        print(Fore.LIGHTBLACK_EX + "-" * 50)
        print(Fore.LIGHTRED_EX + f"Target =\t{target[0]}")
        print(Fore.LIGHTBLACK_EX + "-" * 50)
        print(Fore.LIGHTBLUE_EX + ">>>\tSecond Innings\t<<<\n")
        Scorcard(bn, b, target2[0], target2[1])

    else:
        target = firstInn(o, b, n, batsman)
        print(Fore.LIGHTRED_EX + f"Score :\t {target[0]}/{target[1]}")
        print(Fore.LIGHTBLACK_EX + "-" * 50)
        print(Fore.LIGHTRED_EX + f"\t<-- Target = {target[0]} -->")
        print(Fore.LIGHTBLACK_EX + "-" * 50)
        target2 = secondInn(o, pl, n, "player", target[0])
        print(LIGHTBLACK_EX + f"\n{'-'*50}")
        print(Fore.BLUE + "\t<<<<< SCOREBOARD >>>>>")
        print(Fore.LIGHTBLACK_EX + "-" * 50)
        print(Fore.LIGHTBLUE_EX + ">>>\tFirst Innings\t<<<\n")
        Scorcard(bn, b, target[0], target[1])
        print(Fore.LIGHTBLACK_EX + "-" * 50)
        print(Fore.LIGHTRED_EX + f"\nTarget =\t{target[0]}\n")
        print(Fore.LIGHTBLACK_EX + "-" * 50)
        print(Fore.LIGHTBLUE_EX + ">>>\tSecond Innings\t<<<\n")
        Scorcard(pn, pl, target2[0], target2[1])

    print(Fore.LIGHTMAGENTA_EX + "*" * 50)
    print(Fore.LIGHTRED_EX + "\t>>>>> E.O.M. <<<<<")
    print(Fore.LIGHTMAGENTA_EX + f"{'*'*50}\n")
    if platform.system() == "Windows":
        playsound(".\\assets\\gameOver.mp3")
    else:
        playsound("./assets/gameOver.mp3")
    print(Fore.RESET)