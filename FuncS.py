import platform
import random
import time

from playsound import playsound

 
def bot():
    return random.randint(0,6)


def botname(n,ln):
    for i in range(n):
        s=f"Bot{i+1}"
        ln.append(s)
        s=""


def toss():
    return random.randint(0,1)


def inputR(min,max):
    n=int(input("Move :"))
    if n<=max and n>=min:
        return n
    else:
        print("X")
        return inputR(min,max)


def inputR2(min):
    n=int(input("Enter the numbers of players playing (greater than 1) :"))
    if n>=min:
        return n
    else:
        print("It is smaller than 2 ,try again !")
        return inputR2(min)


def addPlayerName(n,li):
    for i in range(n):
        name=input(f"Enter {i+1} player name :")
        li.append(name)


def firstInn(overs,l,p,batsman):
    print("-"*50)
    print("\n\t<---- 1st Innings ---->\n")
    print("-"*50)
    total=0
    score=0
    c=0
    overC=0
    for ball in range(overs*6):
        move=inputR(0,6)
        bots=bot()
        print(f"bot :{bots}")
        if move==bots:
            l[c]=score
            c=c+1
            print("out")
            total=total+score
            score=0
            if c==p:
                print("All out")
                break
        else:
            if batsman == 'player':
                score=score+move
            else :
                score=score+bots
        
        if (ball+1)%6==0:
            overC+=1
            print(f"overs : {overC}.{(ball+1)%6}")
        else:
            print(f"overs : {overC}.{(ball+1)%6}")
    
    if c<p:
        l[c]=score
        total=total+score
    
    print("-"*50)    
    print("\t<---- 1st Innings END ---->")
    print("-"*50)
    return [total,c]


def secondInn(overs, l, p, batsman, target):
    print("-"*50)
    print("\n\t<---- 2nd Innings ---->\n")
    print("-"*50)
    total=0
    score=0
    c=0
    overC=0
    flag=True
    for ball in range(overs*6):
        if total < target:
            move=inputR(0,6)
            bots=bot()
            print(f"bot :{bots}")
            #overs printing
            if (ball+1)%6==0:
                overC+=1
                print(f"over : {overC}.{(ball+1)%6}")
            else:
                print(f"over : {overC}.{(ball+1)%6}")
            
            if batsman=='player':
                total=total+move
            else :
                total=total+bots
            
            if move==bots:
                l[c]=score
                c+=1
                print("out")

                score=0
                if c==p and total<target:
                    print("All out!!")
                    print("-"*50)
                    print(f"Score :\t {total}/{c}")
                    print("-"*50)
                    if batsman=='player':
                        print(f"\n\t<-- Opponent won by {target-total} runs! -->")
                        print("-"*50)
                        if platform.system()=='Windows':
                            playsound('.\\assets\\clappingLose.wav')
                        else:
                            playsound('./assets/clappingLose.wav')
                    else :
                        print(f"\t<-- You won by {target-total} runs! -->")
                        print("-"*50)
                        if platform.system()=='Windows':
                            playsound('.\\assets\\clappingWin.wav')
                        else:
                            playsound('./assets/clappingWin.wav')
                    flag=False
                    break
                
            else:
                if batsman == 'player':
                    score=score+move
                else :
                    score=score+bots

        elif total==target and c==p:
            print("-"*50)
            print(f"Score :\t {total}/{c}")
            print("-"*50)
            print("\t<-- Match Draw -->")
            print("-"*50)
            break

        else:
            print("-"*50)
            print(f"Score :\t {total}/{c}")
            print("-"*50)
            if batsman=='player':
                print(f"\n\t<-- You won by {p-c} wickets -->")
                print("-"*50)
                if platform.system()=='Windows':
                    playsound('.\\assets\\clappingWin.wav')
                else:
                    playsound('./assets/clappingWin.wav')

            else :
                print(f"\n\t<-- You lost by {p-c} wickets -->")
                print("-"*50)
                if platform.system()=='Windows':
                    playsound('.\\assets\\clappingLose.wav')
                else:
                    playsound('./assets/clappingLose.wav')
            break


    if total < target and flag:
        print("-"*50)
        print(f"Score :\t {total}/{c}")
        print("-"*50)
        print("\t<--- Overs Ended --->")
        print("-"*50)
        if batsman=='player':
            print(f"\t<-- Opponent won by {target-total} runs! -->")
            print("-"*50)
            if platform.system()=='Windows':
                playsound('.\\assets\\clappingLose.wav')
            else:
                playsound('./assets/clappingLose.wav')
        else :
            print(f"\t<-- You won by {target-total} runs! -->")
            print("-"*50)
            if platform.system()=='Windows':
                playsound('.\\assets\\clappingWin.wav')
            else:
                playsound('./assets/clappingWin.wav')
    
    if c<p:
        l[c]=score

    return [total,c]


def matchStart():
    print("\n<-- Note : Please use exact phrase for the options -->\n")
    print("\t<---   Welcome to the toss   --->\n")
    tossOut=toss()
    if random.randint(0,1)==0:
        print("You will choose ! \n")
        ch1=input("HEADS or TAILS :")
        
        print("\n\t*Coin flicks\n")
        #coin flip sound
        if platform.system()=='Windows':
            playsound('.\\assets\\coinflip.wav')
        else:
            playsound('./assets/coinflip.wav')
        
        if (((ch1.upper()).lstrip()).rstrip())=="HEADS" and tossOut==0:
            print("\t<-- You won the toss! -->")
            ch2=input("BAT or BOWL :")
            if (((ch2.upper()).lstrip()).rstrip())=="BAT":
                return "player"
            else:
                return "bot"
        else:
            print("Bot Won the toss!")
            ch2=random.randint(0,1)
            if ch2==0 :
                time.sleep(random.randint(1, 2))
                print("Bot chose to bowl first!")
                return "player"
            else:
                time.sleep(random.randint(1, 2))
                print("Bot chose to bat first!")
                return "bot"
    else:
        print("Bot will choose \n")
        ch1=random.randint(0,1)
        if ch1==0:
            time.sleep(random.randint(1, 2))
            print("Bot chose HEADS.")
        else:
            time.sleep(random.randint(1, 2))
            print("Bot chose TAILS.")
        
        print("\n\t*Coin flicks\n")
        #coin flip sound
        if platform.system()=="Windows":
            playsound('.\\assets\\coinflip.wav')
        else:
            playsound('./assets/coinflip.wav')
        
        ch2=random.randint(0,1)
        if ch2==0 and tossOut==0:
            print("Bot Won!")
            ch2=random.randint(0, 1)
            if ch2==1:
                time.sleep(random.randint(1, 2))
                print("Bot opt to bowl.")
                return "player"
            else:
                time.sleep(random.randint(1, 2))
                print("Bot opt to bat.")
                return "bot"
        else:
            print("Bot lost the toss!")
            print("Please Choose.")
            ch3=input("BAT or BOWL :")    
            if (((ch3.upper()).lstrip()).rstrip())=="BAT":
                return "player"
            else:
                return "bot"


def Scorcard(ln,ls,Score,wicket):
    n=len(ls)
    for i in range(n):
        print(f"{ln[i]} Scored -->\t {ls[i]}")
    print(f"total = \t {Score}/{wicket}")

