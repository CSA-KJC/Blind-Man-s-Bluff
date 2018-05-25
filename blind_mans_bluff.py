##                 GNU GENERAL PUBLIC LICENSE
##                   Version 3, 29 June 2007
##
##Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
##Everyone is permitted to copy and distribute verbatim copies
##of this license document, but changing it is not allowed.
##
##                        Preamble
##
##The GNU General Public License is a free, copyleft license for
##software and other kinds of works.
##
##The licenses for most software and other practical works are designed
##to take away your freedom to share and change the works.  By contrast,
##the GNU General Public License is intended to guarantee your freedom to
##share and change all versions of a program--to make sure it remains free
##software for all its users.  We, the Free Software Foundation, use the
##GNU General Public License for most of our software; it applies also to
##any other work released this way by its authors.  You can apply it to
##your programs, too.

#Katie Chiu
#Blind Man's Bluff. Last update 5/24/18
#BETA FINISHED
#Might clean up some things to make code shorter or find unused variables

#Simple text-based card game with 3 other players (No AI), bet with money
#You can call, bet, or fold
#No audio, may add soon
#Shows high scores (on separate file) and instructions
#Cards are randomly assigned

import random
import os
import sys
import time
global cards
global face
global p1
global p2
global p3
global p1call
global p2call
global p3call
global youcall
global you
global p1money
global p2money
global p3money
global money
global p1_bet,p2_bet,p3_bet
global fold
global greatest
global call
global current
global rounds
global youbet
global total
face={11:"jack", 12:"queen", 13:"king", 14:"ace"}
shape={1:"hearts", 2:"diamonds", 3:"spades", 4:"clubs"}
p1=[]
p2=[]
p3=[]
you=[]
fold=[]
p1call=[-1]
p2call=[-2]
p3call=[-3]
youcall=[-4]
greatest=[]
current=0
rounds=0
p1money=int(975)
p2money=int(975)
p3money=int(975)
youbet=0
money=1000
start=0
total=0

def distribute(money):
    global p1
    global p2
    global p3
    global fold
    global p1call
    global p2call
    global p3call
    global youcall
    global p1_bet
    global p2_bet
    global p3_bet
    global greatest
    global current
    global rounds
    global p1money
    global p2money
    global p3money
    global total
    global you
    fold=[]
    p1call=[-1]
    p2call=[-2]
    p3call=[-3]
    youcall=[-4]
    p1_bet=0
    p2_bet=0
    p3_bet=0
    greatest=[]
    current=0
    rounds=0
    p1money=975
    p2money=975
    p3money=975
    start=0
    total=0
    you=[]
    p1=[]
    p2=[]
    p3=[]

    for x in range(4):
        prob=random.random() #creates random numbers for random cards
        value=random.randrange(2,15)
        num=random.randrange(1,5)
        card=shape[num]
        greatest.append(value)
        if x==1: #for each player it assigns a card
            p1.append(card)
            p1.append(value)
            p=Player1(p1,value,p1money,current) #goes to player 1's class
            print(p)
        elif x==2:
            p2.append(card)
            p2.append(value)
            q=Player2(p2,value,p2money,current) #goes to player 2's class
            print(q)
        elif x==3:
            p3.append(card)
            p3.append(value)
            y=Player3(p3,value,p3money,current) #goes to player 3's class
            print(y)
        else:
            you.append(card)
            you.append(value)
            if you[1]>=11: #if it is a face card
                number=face[value]
                del you[1]
                you.append(number)
            else:
                pass
    action(start)

class Player1:
    def __init__(self, initp1, initvalue,initp1money,initcurrent): #transfers values into class
        self.p1=initp1
        self.value=initvalue
        self.p1money=initp1money
        return(Player1.add(self)) #goes to next function
    def add(self): #adds it to list
        if self.p1[1]>=11: #if it is a face card
            number=face[self.value]
            self.p1.append(number)
    def action(self):
        global current
        global rounds
        global total
        global p1_bet
        global money
        global p1money
        if p1money<current:
            prob=random.random()
            move=random.randrange(2,4)
        elif money==current:
            prob=random.random()
            move=random.randrange(2,4)
        else:
            prob=random.random()
            move=random.randrange(1,4) #to choose what to do
        if move==1: #bet
            rounds=rounds+1
            amount=random.randrange(current,self) #how much to bet
            if current==amount:
                p1call.append(rounds)
                p1_bet=current
                return("Player 1 decided to call with $"+str(p1_bet)+" and has $"+str(self-current)+" left.")
            else:
                current=amount #keep track of how much each person has bet
                total=total+amount
                return("Player 1 is betting $"+str(current)+" and has $"+str(self-current)+" left.")
        elif move==2: #call
            p1call.append(rounds)
            p1_bet=current
            if current>p1money:
                p1money=0
                p1_bet=975
                return("Player 1 decided to call with $"+str(p1_bet)+" and has $"+str(p1money)+" left.")
            else:
                return("Player 1 decided to call with $"+str(p1_bet)+" and has $"+str(self-current)+" left.")
        elif move==3:
            fold.append("1") #to fold
            p1call.append(rounds)
            return("Player 1 decided to fold and is out of the game.")
    def __str__(self):
        return("Player 1: "+str(self.p1[-1])+" of "+str(self.p1[0])) #lets user know what card player 1 has

class Player2:
    def __init__(self, initp2, initvalue, initp2money,initcurrent): #transfers values into class
        self.p2=initp2
        self.value=initvalue
        self.p2money=initp2money
        return(Player2.add(self)) #goes to next function
    def add(self): #adds it to list
        if self.p2[1]>=11: #if it is a face card
            number=face[self.value]
            self.p2.append(number)
    def action(self):
        global current
        global rounds
        global total
        global p2_bet
        global money
        global p2money
        if p2money<current:
            prob=random.random()
            move=random.randrange(2,4)
        elif money==current:
            prob=random.random()
            move=random.randrange(2,4)
        else:
            prob=random.random()
            move=random.randrange(1,4) #to choose what to do
        if move==1: #bet
            rounds=rounds+1
            amount=random.randrange(current,self) #how much to bet
            if current==amount:
                p2call.append(rounds)
                p2_bet=current
                return("Player 2 decided to call with $"+str(p2_bet)+" and has $"+str(self-current)+" left.")
            else:
                total=total+amount
                current=amount #keep track of how much each person has bet
                return("Player 2 is betting $"+str(current)+" and has $"+str(self-current)+" left.")
        elif move==2: #call
            p2call.append(rounds)
            p2_bet=current
            if current>p2money:
                p2money=0
                p2_bet=975
                return("Player 2 decided to call with $"+str(p2_bet)+" and has $"+str(p2money)+" left.")
            else:
                return("Player 2 decided to call with $"+str(p2_bet)+" and has $"+str(self-current)+" left.")
        elif move==3: #fold
            fold.append("2")
            p2call.append(rounds)
            return("Player 2 decided to fold and is out of the game.")
    def __str__(self):
        return("Player 2: "+str(self.p2[-1])+" of "+str(self.p2[0])) #lets user know what card player 2 has

class Player3:
    def __init__(self, initp3,initvalue, initp3money,initcurrent): #transfers values into class
        self.p3=initp3
        self.value=initvalue
        self.p3money=initp3money
        return(Player3.add(self)) #goes to next funciton
    def add(self): #adds to list
        if self.p3[1]>=11: #if it is a face card
            number=face[self.value]
            self.p3.append(number)
    def action(self):
        global current
        global rounds
        global total
        global p3_bet
        global p3money
        if p3money<current:
            prob=random.random()
            move=random.randrange(2,4)
        elif p3money==current:
            prob=random.random()
            move=random.randrange(2,4)
        else:
            prob=random.random()
            move=random.randrange(1,4) #to choose what to do
        if move==1: #bet
            rounds=rounds+1
            amount=random.randrange(current,self) #how much to bet
            if current==amount:
                p3call.append(rounds)
                p3_bet=current
                return("Player 3 decided to call with $"+str(p3_bet)+" and has $"+str(self-current)+"left.")
            else:
                total=total+amount
                current=amount #keep track of how much each person has bet
                return("Player 3 is betting $"+str(current)+" and has $"+str(self-current)+" left.")
        elif move==2: #call
            p3call.append(rounds)
            p3_bet=current
            if current>p3money:
                p3money=0
                p3_bet=975
                return("Player 3 decided to call with $"+str(p3_bet)+" and has $"+str(p3money)+" left.")
            else:
                return("Player 3 decided to call with $"+str(p3_bet)+" and has $"+str(self-current)+" left.")
        elif move==3: #fold
            fold.append("3")
            p3call.append(rounds)
            return("Player 3 decided to fold and is out of the game.")
    def __str__(self):
        return("Player 3: "+str(self.p3[-1])+" of "+str(self.p3[0])) #lets user know what card player 3 has


def action(start):
    global money
    global fold
    global call
    global current
    global total
    global p1_bet
    global p2_bet
    global p3_bet
    if start==0: #beginning of game
        start=1
        money=int(money)-25 #start money
        print("You put $25 into the pot to start. You have $"+str(money)+" left") #keeping track of their money
        action(start)
    else:
        if fold.count("1")==1 and fold.count("2")==1 and fold.count("3")==1: #if everyone has folded
            money=money+p1_bet+p2_bet+p3_bet+100
            print("Congratulations! You have won the game with $"+str(money)+"\n")
            time.sleep(2)
            nextaction()
        elif p1call[-1]==p2call[-1] and p2call[-1]==p3call[-1] and p3call[-1]==youcall[-1]:
            finish(start)
        else:
            if current<money:
                play=input("What would you like to do?\n1. Bet\n2. Call\n3. Fold\n") #displaying options
                if play=="1":
                    start=2
                    bet(start)
                elif play=="2":
                    if start==1:
                        print("You cannot call on the first move\n")
                        time.sleep(1)
                        action(start)
                    else:
                        call(start)
                elif play=="3":
                    youfold()
                else: #if they don't input 1, 2, or 3
                    print("That is not an option\n")
                    time.sleep(1)
                    action(start)
            else:
                play=input("You do not have enough money to bet. You can only\n1. Call\n2. Fold\n")
                if play=="1":
                    start=2
                    call(start)
                elif play=="2":
                    youfold()
                else:
                    print("That is not an option\n")
                    time.sleep(1)
                    action(start)

def bet(start): #when the user wants to bet
    global money
    global current
    global rounds
    global youbet
    rounds=rounds+1
    try:
        amount=int(input("You have $"+str(money-current)+". How much would you like to put in? ")) #asks user for amount of money
    except ValueError: #if they don't input integer
        print("That isn't a whole number\n")
        time.sleep(1)
        action(start)
    if amount>(money-current): #if user inputs more money than they have
        print("You don't have that much money. Try again\n")
        time.sleep(1)
        bet(start)
    elif amount<=0: #if user inputs 0 or less
        print("That isn't enough money. Try again\n")
        time.sleep(1)
        action(start)
    else:
        current=current+amount
        print("You are now betting $"+str(current)+". You now have $"+str(money-current))
        p_action(start)

def call(start): #call
    global money
    global current
    global rounds
    global p1call
    global p2call
    global p3call
    global youcall
    global you
    youcall.append(rounds)
    if current>money:
        print("You have $0 left")
        money=0
        if p1call[-1]==p2call[-1] and p2call[-1]==p3call[-1] and p3call[-1]==youcall[-1]:
            finish(start) 
        else:
            p_action(start)
    else:
        print("You have $"+str(money-current)+" left")
        if p1call[-1]==p2call[-1] and p2call[-1]==p3call[-1] and p3call[-1]==youcall[-1]:
            finish(start) 
        else:
            p_action(start)
    
def youfold():
    global money
    global current
    global fold
    global greatest
    if money>0:
        money=money-current
    elif money==0:
        print("You have left the game with $"+str(money))
    elif money<0:
        print("broken")
    else:
        print("wat")
    del greatest[0]
    while fold:
        if fold.count("3")==0 and fold.count("2")==0 and fold.count("1")==0:
            break
        if fold.count("3")==1 and fold.count("2")==1:
            del greatest[-1]
            del greatest[-1]
            break
        elif fold.count("2") and fold.count("1")==1:
            del greatest[0]
            del greatest[0]
            break
        elif fold.count("3")==1 and fold.count("1")==1:
            del greatest[-1]
            del greatest[0]
            break
        elif fold.count("1")==1:
            del greatest[0]
            break
        elif fold.count("2")==1:
            del greatest[1]
            break
        elif fold.count("3")==1:
            del greatest[2]
            break
    highest=max(greatest)
    place=greatest.index(highest)
    if place==0:
        print("Player 1 has won the game\n")
    elif place==1:
        print("Player 2 has won the game\n")
    elif place==2:
        print("Player 3 has won the game\n")
    time.sleep(2)
    os.system('cls')
    menu()

def p_action(start):
    global p1money
    global p2money
    global p3money
    global current
    global total
    start=2
    if fold.count("1")==0 and fold.count("2")==0 and fold.count("3")==0: #if no one has folded
        print(Player1.action(p1money))
        time.sleep(0.75)
        if p1call[-1]==p2call[-1] and p2call[-1]==p3call[-1] and p3call[-1]==youcall[-1]:
            finish(start)
        else:
            print(Player2.action(p2money))
            time.sleep(0.75)
            if p1call[-1]==p2call[-1] and p2call[-1]==p3call[-1] and p3call[-1]==youcall[-1]:
                finish(start)
            else:
                print(Player3.action(p3money))
                time.sleep(0.75)
                print("The current bet is at $"+str(current)+"\n")
                if p1call[-1]==p2call[-1] and p2call[-1]==p3call[-1] and p3call[-1]==youcall[-1]:
                    finish(start)
                else:
                    action(start)
    elif fold.count("1")==0 and fold.count("2")==0 and fold.count("3")==1: #if player 3 has folded
        print(Player1.action(p1money))
        time.sleep(0.75)
        if p1call[-1]==p2call[-1] and p2call[-1]==p3call[-1] and p3call[-1]==youcall[-1]:
            finish(start)
        else:
            print(Player2.action(p2money))
            time.sleep(0.75)
            if p1call[-1]==p2call[-1] and p2call[-1]==p3call[-1] and p3call[-1]==youcall[-1]:
                finish(start)
            else:
                p3call.append(rounds)
                print("The current bet is at $"+str(current)+"\n")
                if p1call[-1]==p2call[-1] and p2call[-1]==p3call[-1] and p3call[-1]==youcall[-1]:
                    finish(start)
                else:
                    action(start)
    elif fold.count("1")==0 and fold.count("2")==1 and fold.count("3")==1: #if players 2 and 3 have folded
        print(Player1.action(p1money))
        time.sleep(0.75)
        if p1call[-1]==p2call[-1] and p2call[-1]==p3call[-1] and p3call[-1]==youcall[-1]:
            finish(start)
        else:
            p2call.append(rounds)
            p3call.append(rounds)
            print("The current bet is at $"+str(current)+"\n")
            if p1call[-1]==p2call[-1] and p2call[-1]==p3call[-1] and p3call[-1]==youcall[-1]:
                    finish(start)
            else:
                action(start)
    elif fold.count("1")==1 and fold.count("2")==0 and fold.count("3")==0: #if player 1 has folded
        print(Player2.action(p2money))
        time.sleep(0.75)
        if p1call[-1]==p2call[-1] and p2call[-1]==p3call[-1] and p3call[-1]==youcall[-1]:
            finish(start)
        else:
            print(Player3.action(p3money))
            time.sleep(0.75)
            if p1call[-1]==p2call[-1] and p2call[-1]==p3call[-1] and p3call[-1]==youcall[-1]:
                finish(start)
            else:
                p1call.append(rounds)
                print("The current bet is at $"+str(current)+"\n")
                if p1call[-1]==p2call[-1] and p2call[-1]==p3call[-1] and p3call[-1]==youcall[-1]:
                    finish(start)
                else:
                    action(start)
    elif fold.count("1")==1 and fold.count("2")==1 and fold.count("3")==0: #if players 1 and 2 have folded
        print(Player3.action(p3money))
        time.sleep(0.75)
        if p1call[-1]==p2call[-1] and p2call[-1]==p3call[-1] and p3call[-1]==youcall[-1]:
            finish(start)
        else:
            p1call.append(rounds)
            p2call.append(rounds)
            print("The current bet is at $"+str(current)+"\n")
            if p1call[-1]==p2call[-1] and p2call[-1]==p3call[-1] and p3call[-1]==youcall[-1]:
                    finish(start)
            else:
                action(start)
    elif fold.count("1")==0 and fold.count("2")==1 and fold.count("3")==0: #if player 2 has folded
        print(Player1.action(p1money))
        time.sleep(0.75)
        if p1call[-1]==p2call[-1] and p2call[-1]==p3call[-1] and p3call[-1]==youcall[-1]:
            finish(start)
        else:
            print(Player3.action(p3money))
            time.sleep(0.75)
            p2call.append(rounds)
            print("The current bet is at $"+str(current)+"\n")
            if p1call[-1]==p2call[-1] and p2call[-1]==p3call[-1] and p3call[-1]==youcall[-1]:
                    finish(start)
            else:
                action(start)
    elif fold.count("1")==1 and fold.count("2")==0 and fold.count("3")==1: #if players 1 and 3 have folded
        print(Player2.action(p2money))
        time.sleep(0.75)
        if p1call[-1]==p2call[-1] and p2call[-1]==p3call[-1] and p3call[-1]==youcall[-1]:
            finish(start)
        else:
            p1call.append(rounds)
            p3call.append(rounds)
            print("The current bet is at $"+str(current)+"\n")
            if p1call[-1]==p2call[-1] and p2call[-1]==p3call[-1] and p3call[-1]==youcall[-1]:
                    finish(start)
            else:
                action(start)
    
def finish(start):
    global fold
    global p1_bet
    global p2_bet
    global p3_bet
    global money
    global current
    if fold.count("1")==1 and fold.count("2")==1 and fold.count("3")==1:
        action(start)
    else:
        while money:
            if fold.count("3")==1 and fold.count("2")==1:
                del greatest[-1]
                del greatest[-1]
                highest=max(greatest)
                place=greatest.index(highest)
                if place==1:
                    print("Player 1 won the game\n")
                    money=money-current
                    time.sleep(2)
                    again()
                elif place==0:
                    money=p1_bet+p2_bet+p3_bet+money+100
                    print("You have won the game with $"+str(money)+"\n")
                    time.sleep(2)
                    nextaction()
            elif fold.count("2")==1 and fold.count("1")==1:
                del greatest[1]
                del greatest[1]
                highest=max(greatest)
                place=greatest.index(highest)
                if place==1:
                    print("Player 3 won the game\n")
                    money=money-current
                    time.sleep(2)
                    again()
                elif place==0:
                    money=p1_bet+p2_bet+p3_bet+money+100
                    print("You have won the game with $"+str(money)+"\n")
                    time.sleep(2)
                    nextaction()
            elif fold.count("3")==1 and fold.count("1")==1:
                del greatest[-1]
                del greatest[1]
                highest=max(greatest)
                place=greatest.index(highest)
                if place==1:
                    print("Player 2 won the game\n")
                    money=money-current
                    time.sleep(2)
                    again()
                elif place==0:
                    money=p1_bet+p2_bet+p3_bet+money+100
                    print("You have won the game with $"+str(money)+"\n")
                    time.sleep(2)
                    nextaction()
            elif fold.count("1")==1:
                del greatest[1]
                highest=max(greatest)
                place=greatest.index(highest)
                if place==1:
                    print("Player 2 won the game\n")
                    money=money-current
                    time.sleep(2)
                    again()
                elif place==2:
                    print("Player 3 won the game\n")
                    money=money-current
                    time.sleep(2)
                    again()
                elif place==0:
                    money=p1_bet+p2_bet+p3_bet+money+100
                    print("You have won the game with $"+str(money)+"\n")
                    time.sleep(2)
                    nextaction()
            elif fold.count("2")==1:
                del greatest[2]
                highest=max(greatest)
                place=greatest.index(highest)
                if place==1:
                    print("Player 1 won the game\n")
                    money=money-current
                    time.sleep(2)
                    again()
                elif place==3:
                    print("Player 3 won the game\n")
                    money=money-current
                    time.sleep(2)
                    again()
                elif place==0:
                    money=p1_bet+p2_bet+p3_bet+money+100
                    print("You have won the game with $"+str(money)+"\n")
                    time.sleep(2)
                    nextaction()
            elif fold.count("3")==1:
                del greatest[3]
                highest=max(greatest)
                place=greatest.index(highest)
                if place==1:
                    print("Player 1 won the game\n")
                    money=money-current
                    time.sleep(2)
                    again()
                elif place==2:
                    print("Player 2 won the game\n")
                    money=money-current
                    time.sleep(2)
                    again()
                elif place==0:
                    money=p1_bet+p2_bet+p3_bet+money+100
                    print("You have won the game with $"+str(money)+"\n")
                    time.sleep(2)
                    nextaction()
            else:
                highest=max(greatest)
                place=greatest.index(highest)
                if place==1:
                    print("Player 1 won the game\n")
                    money=money-current
                    time.sleep(2)
                    again()
                elif place==2:
                    print("Player 2 won the game\n")
                    money=money-current
                    time.sleep(2)
                    again()
                elif place==0:
                    money=p1_bet+p2_bet+p3_bet+money+100
                    print("You have won the game with $"+str(money)+"\n")
                    time.sleep(2)
                    nextaction()

def nextaction():
    global money
    scores=[]
    if money<=0:
        menu()
    else:
        file=open("highscores.txt","r")
        x=file.readline()
        while x:
            x=list(x)
            del x[-1]
            x=("").join(x)
            scores.append(x)
            x=file.readline()
        file.close()
        for z in scores:
            place=scores.index(z)
            try:
                even=int(place/2)
                if money>int(z):
                    addscore()
            except ValueError:
                pass 
    again()

def menu():
    global p1print
    global p2print
    global p3print
    global money
    print("Welcome to Blind Man's Bluff!")
    print("1. Start game\n2. Instructions\n3. High Scores\n4. Exit")
    choice=input("What would you like to do? ")
    if choice=="1":
        os.system('cls')
        money=1000
        distribute(money)
    elif choice=="2":
        os.system('cls')
        explain()
    elif choice=="3":
        os.system('cls')
        record()
    elif choice=="4":
        os.system('cls')
        sys.exit()
    else:
        print("That is not a choice\n")
        time.sleep(2)
        os.system('cls')
        menu()

def record():
    print("HIGH SCORES")
    scores=open("highscores.txt","r")
    x=scores.readline()
    place=[]
    while x:
        place.append(x)
        score=place.index(x)
        if (score%2)!=0:
            print(x)
            x=scores.readline()
        else:
            x=list(x)
            del x[-1]
            x=("").join(x)
            print(x)
            x=scores.readline()
    scores.close()
    choice=input("Enter 1 to return to menu\n")
    if choice=="1":
        os.system('cls')
        menu()
    else:
        print("That is not a choice")
        time.sleep(2)
        os.system('cls')
        record()

def addscore():
    global money
    scores=[]
    print("Congratulations! You have a new high score!")
    name=input("What is your name? ")
    file=open("highscores.txt","r")
    x=file.readline()
    while x:
        x=list(x)
        del x[-1]
        x=("").join(x)
        scores.append(x)
        x=file.readline()
    file.close()

    scores.append(name)
    scores.append(money)
    file1=open("highscores.txt","w")
    for i in scores:
        file1.write(str(i))
        file1.write("\n")
    file1.close()
    scores=open("highscores.txt","r")
    print("HIGH SCORES")
    x=scores.readline()
    place=[]
    while x:
        place.append(x)
        score=place.index(x)
        if (score%2)!=0:
            print(x)
            x=scores.readline()
        else:
            x=list(x)
            del x[-1]
            x=("").join(x)
            print(x)
            x=scores.readline()
    scores.close()
    again()

def again():
    global money
    if money>25:
        option=input("Would you like to\n1. Play again with same amount of money\n2. Go to menu\n3. Play again\n")
        if option=="1":
            os.system("cls")
            distribute(money)
        elif option=="2":
            os.system("cls")
            menu()
        elif option=="3":
            os.system("cls")
            money=1000
            distribute(money)
        else:
            print("That is not an option\n")
            time.sleep(1)
            again()
    else:
        os.system("cls")
        menu()

def start():
    file=open("highscores.txt","w")
    file.write("Jenny\n1000\nMark\n943\n")
    file.close()
    menu()

def explain():
    print("This game is similar to poker where you bet, however, each player puts their card on their forehead.")
    print("Each player can see everyone's card except their own.\nWhen starting the game, each player starts with $1000 and puts in $25 to start.")
    print("The game ends when everyone folds, everyone calls, or you fold.")
    print("If you run out of money, you only have the option of calling or folding.\nIf you call you end up with $0 for the rest of the game.")
    print("The person with the highest card wins the game.\n")
    leave=input("Enter 1 to go back to menu ")
    if leave=="1":
        os.system("cls")
        menu()
    else:
        print("That is not an option")
        time.sleep(2)
        os.system("cls")
        explain()

start()
