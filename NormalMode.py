from FuncS import *


def normal():
    print(f"\n{'+'*50}")
    print("<<<<<<<<<<\t WELCOME \t>>>>>>>>>>")
    print(f"{'+'*50}")
    # input for overs and number of players
    o=int(input("\nEnter the number of Overs :"))
    n=inputR2(2)
    #lists for Scorcard and player names
    pn=[]
    bn=[]
    pl=[0]*n
    b=[0]*n
    print(f"\n{'~'*50}")
    print("<--  Please enter the names of the players -->")
    print(f"{'-'*50}\n")
    addPlayerName(n,pn)
    botname(n, bn)
    print(f"\n{'^'*50}")
    batsman=matchStart()
    
    if batsman=='player':
        target=firstInn(o, pl, n, batsman)
        print(f"Score :\t {target[0]}/{target[1]}")
        print("-"*50)
        print(f"\t<-- Target = {target[0]} -->")
        print("-"*50)
        target2=secondInn(o, b, n, "bot", target[0])
        print(f"\n{'-'*50}")
        print("\t<<<<< SCOREBOARD >>>>>")
        print("-"*50)
        print(">>>\tFirst Innings\t<<<\n")
        Scorcard(pn, pl , target[0], target[1])
        print("-"*50)
        print(f"Target =\t{target[0]}")
        print("-"*50)
        print(">>>\tSecond Innings\t<<<\n")
        Scorcard(bn, b , target2[0], target2[1])
    
    else:
        target=firstInn(o, b, n, batsman)
        print(f"Score :\t {target[0]}/{target[1]}")
        print("-"*50)
        print(f"\t<-- Target = {target[0]} -->")
        print("-"*50)
        target2=secondInn(o, pl, n, "player", target[0])
        print(f"\n{'-'*50}")
        print("\t<<<<< SCOREBOARD >>>>>")
        print("-"*50)
        print(">>>\tFirst Innings\t<<<\n")
        Scorcard(bn, b, target[0], target[1])
        print("-"*50)
        print(f"\nTarget =\t{target[0]}\n")
        print("-"*50)
        print(">>>\tSecond Innings\t<<<\n")
        Scorcard(pn, pl , target2[0], target2 [1])
    
    print("*"*50)
    print("\t>>>>> E.O.M. <<<<<")
    print(f"{'*'*50}\n")
    
    if platform.system()=="Windows":
        playsound('.\\assets\\gameOver.mp3')
    else:
        playsound('./assets/gameOver.mp3')