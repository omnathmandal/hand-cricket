import platform
import random
import time

from colorama import Fore, Back, Style
from playsound import playsound

def bot() -> int:
    return random.randint(0, 6)


def botname(n: int, ln: list) -> None:
    for i in range(n):
        s = f"Bot{i+1}"
        ln.append(s)
        s = ""


def toss() -> int:
    return random.randint(0, 1)


def inputR(min: int, max: int) -> int:
    n = int(input(Fore.GREEN + "Move :"))
    if n <= max and n >= min:
        return n
    else:
        print(Fore.RED + "X")
        return inputR(min, max)


def inputR2(min: int) -> int:
    n = int(input(Fore.YELLOW + "Enter the numbers of players playing (greater than 1) :"))
    if n >= min:
        return n
    else:
        print(Fore.RED + "It is smaller than 2 ,try again !")
        return inputR2(min)


def addPlayerName(n: int, li: list) -> None:
    for i in range(n):
        name = input(Fore.LIGHTMAGENTA_EX + f"Enter {i+1} player name :")
        li.append(name)


def firstInn(overs: int, l: list, p: int, batsman: str) -> list:
    print(Fore.LIGHTBLACK_EX + "-" * 50)
    print(Fore.LIGHTBLACK_EX + "\n\t<---- 1st Innings ---->\n")
    print(Fore.LIGHTBLACK_EX + "-" * 50)
    total = 0
    score = 0
    c = 0
    overC = 0
    for ball in range(overs * 6):
        move = inputR(0, 6)
        bots = bot()
        print(Fore.LIGHTBLUE_EX + f"bot :{bots}")
        if move == bots:
            l[c] = score
            c = c + 1
            print(Fore.RED + "out")
            total = total + score
            score = 0
            if c == p:
                print(Fore.RED + "All out")
                break
        else:
            if batsman == "player":
                score = score + move
            else:
                score = score + bots

        if (ball + 1) % 6 == 0:
            overC += 1
            print(Fore.LIGHTYELLOW_EX + f"overs : {overC}.{(ball+1)%6}")
        else:
            print(Fore.LIGHTYELLOW_EX + f"overs : {overC}.{(ball+1)%6}")

    if c < p:
        l[c] = score
        total = total + score

    print(Fore.LIGHTBLACK_EX + "-" * 50)
    print(Fore.LIGHTBLACK_EX + "\t<---- 1st Innings END ---->")
    print(Fore.LIGHTBLACK_EX + "-" * 50)
    return [total, c]


def secondInn(overs: int, l: list, p: int, batsman: str, target: int) -> int:
    print(Fore.LIGHTBLACK_EX + "-" * 50)
    print(Fore.LIGHTBLACK_EX + "\n\t<---- 2nd Innings ---->\n")
    print(Fore.LIGHTBLACK_EX + "-" * 50)
    total = 0
    score = 0
    c = 0
    overC = 0
    flag = True
    for ball in range(overs * 6):
        if total < target:
            move = inputR(0, 6)
            bots = bot()
            print(Fore.LIGHTBLUE_EX + f"bot :{bots}")
            # overs printing
            if (ball + 1) % 6 == 0:
                overC += 1
                print(Fore.LIGHTYELLOW_EX + f"over : {overC}.{(ball+1)%6}")
            else:
                print(Fore.LIGHTYELLOW_EX + f"over : {overC}.{(ball+1)%6}")

            if batsman == "player":
                total = total + move
            else:
                total = total + bots

            if move == bots:
                l[c] = score
                c += 1
                print(Fore.RED + "out")

                score = 0
                if c == p and total < target:
                    print(Fore.RED + "All out!!")
                    print(Fore.LIGHTBLACK_EX + "-" * 50)
                    print(Fore.LIGHTRED_EX + f"Score :\t {total}/{c}")
                    print(Fore.LIGHTBLACK_EX + "-" * 50)
                    if batsman == "player":
                        print(Fore.LIGHTRED_EX + f"\n\t<-- Opponent won by {target-total} runs! -->")
                        print("-" * 50)
                        if platform.system() == "Windows":
                            playsound(".\\assets\\clappingLose.wav")
                        else:
                            playsound("./assets/clappingLose.wav")
                    else:
                        print(Fore.LIGHTGREEN_EX + f"\t<-- You won by {target-total} runs! -->")
                        print(Fore.LIGHTBLACK_EX + "-" * 50)
                        if platform.system() == "Windows":
                            playsound(".\\assets\\clappingWin.wav")
                        else:
                            playsound("./assets/clappingWin.wav")
                    flag = False
                    break

            else:
                if batsman == "player":
                    score = score + move
                else:
                    score = score + bots

        elif total == target and c == p:
            print(Fore.LIGHTBLACK_EX + "-" * 50)
            print(Fore.LIGHTRED_EX + f"Score :\t {total}/{c}")
            print(Fore.LIGHTBLACK_EX + "-" * 50)
            print(Fore.LIGHTWHITE_EX + "\t<-- Match Draw -->")
            print(Fore.LIGHTBLACK_EX + "-" * 50)
            break

        else:
            print(Fore.LIGHTBLACK_EX + "-" * 50)
            print(Fore.LIGHTRED_EX + f"Score :\t {total}/{c}")
            print(Fore.LIGHTBLACK_EX + "-" * 50)
            if batsman == "player":
                print(Fore.LIGHTGREEN_EX + f"\n\t<-- You won by {p-c} wickets -->")
                print(Fore.LIGHTBLACK_E + "-" * 50)
                if platform.system() == "Windows":
                    playsound(".\\assets\\clappingWin.wav")
                else:
                    playsound("./assets/clappingWin.wav")

            else:
                print(Fore.LIGHTRED_EX + f"\n\t<-- You lost by {p-c} wickets -->")
                print(Fore.LIGHTBLACK_E + "-" * 50)
                if platform.system() == "Windows":
                    playsound(".\\assets\\clappingLose.wav")
                else:
                    playsound("./assets/clappingLose.wav")
            break

    if total < target and flag:
        print(Fore.LIGHTBLACK_E + "-" * 50)
        print(Fore.LIGHTRED_EX + f"Score :\t {total}/{c}")
        print(Fore.LIGHTBLACK_E + "-" * 50)
        print(Fore.LIGHTBLACK_E + "\t<--- Overs Ended --->")
        print(Fore.LIGHTBLACK + "-" * 50)
        if batsman == "player":
            print(Fore.LIGHTRED_EX + f"\t<-- Opponent won by {target-total} runs! -->")
            print(Fore.LIGHTBLACK_E + "-" * 50)
            if platform.system() == "Windows":
                playsound(".\\assets\\clappingLose.wav")
            else:
                playsound("./assets/clappingLose.wav")
        else:
            print(Fore.LIGHTGREEN_EX + f"\t<-- You won by {target-total} runs! -->")
            print(Fore.LIGHTBLACK_E + "-" * 50)
            if platform.system() == "Windows":
                playsound(".\\assets\\clappingWin.wav")
            else:
                playsound("./assets/clappingWin.wav")

    if c < p:
        l[c] = score

    return [total, c]


def matchStart() -> str:
    print(Fore.YELLOW + "\n<-- Note : Please use exact phrase for the options -->\n")
    print(Fore.LIGHTCYAN_EX +"\t<---   Welcome to the toss   --->\n")
    tossOut = toss()
    if random.randint(0, 1) == 0:
        print(Fore.GREEN + "You will choose ! \n")
        ch1 = input(Fore.MAGENTA + "HEADS or TAILS :")

        print(Fore.LIGHTGREEN_EX + "\n\t*Coin flicks\n")
        # coin flip sound
        if platform.system() == "Windows":
            playsound(".\\assets\\coinflip.wav")
        else:
            playsound("./assets/coinflip.wav")

        if (((ch1.upper()).lstrip()).rstrip()) == "HEADS" and tossOut == 0:
            print(Fore.GREEN + "\t<-- You won the toss! -->")
            ch2 = input(Fore.LIGHTYELLOW_EX + "BAT or BOWL :")
            if (((ch2.upper()).lstrip()).rstrip()) == "BAT":
                return "player"
            else:
                return "bot"
        else:
            print(Fore.RED +"Bot Won the toss!")
            ch2 = random.randint(0, 1)
            if ch2 == 0:
                time.sleep(random.randint(1, 2))
                print(Fore.RED +"Bot chose to bowl first!")
                return "player"
            else:
                time.sleep(random.randint(1, 2))
                print(Fore.RED +"Bot chose to bat first!")
                return "bot"
    else:
        print(Fore.LIGHTRED_EX + "Bot will choose \n")
        ch1 = random.randint(0, 1)
        if ch1 == 0:
            time.sleep(random.randint(1, 2))
            print(Fore.LIGHTGREEN_EX + "Bot chose HEADS.")
        else:
            time.sleep(random.randint(1, 2))
            print(Fore.LIGHTGREEN_EX +"Bot chose TAILS.")

        print(Fore.LIGHTGREEN_EX + "\n\t*Coin flicks\n")
        # coin flip sound
        if platform.system() == "Windows":
            playsound(".\\assets\\coinflip.wav")
        else:
            playsound("./assets/coinflip.wav")

        ch2 = random.randint(0, 1)
        if ch2 == 0 and tossOut == 0:
            print(Fore.RED + "Bot Won!")
            ch2 = random.randint(0, 1)
            if ch2 == 1:
                time.sleep(random.randint(1, 2))
                print(Fore.LIGHTRED_EX + "Bot opt to bowl.")
                return "player"
            else:
                time.sleep(random.randint(1, 2))
                print(Fore.LIGHTRED_EX +"Bot opt to bat.")
                return "bot"
        else:
            print(Fore.LIGHTGREEN_EX + "Bot lost the toss!")
            print(Fore.GREEN +"Please Choose.")
            ch3 = input(Fore.LIGHTYELLOW_EX + "BAT or BOWL :")
            if (((ch3.upper()).lstrip()).rstrip()) == "BAT":
                return "player"
            else:
                return "bot"


def Scorcard(ln: list, ls: list, Score: int, wicket: int) -> None:
    n = len(ls)
    for i in range(n):
        print(Fore.YELLOW + f"{ln[i]} Scored --> \t{ls[i]}")
    print(Fore.YELLOW + f"total = \t {Score}/{wicket}")
    
