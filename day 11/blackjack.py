cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
import random
def dealcard():
    card=random.choice(cards)
    return card
def calculatescore(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(userscore,computerscore):
    if userscore==computerscore:
        return "draw"
    elif computerscore ==0:
        return "lose,opponent has Blackjack"
    elif userscore==0:
        return "win with a blackjack"
    elif userscore>21:
        return "you went over, you lose"
    elif computerscore>21:
        return "opponent went over,you win"
    elif userscore>computerscore:
        return "you win"
    else:
        return "you lose" 
def playgame():
    usercard=[]
    computercard=[]
    isgaveover=False
    for _ in range(2):
        usercard.append(dealcard)
        computercard.append(dealcard)

    while not isgaveover:
        userscore=calculatescore(usercard)
        computerscore=calculatescore(computercard)
        print(f" your cards:{usercard},current score:{userscore}")
        print(f"computer's first card: {computercard[0]}")
        if userscore==0 or computerscore==0 or userscore>21:...
        else:...
    while computerscore!=0 and computerscore<17:
        computercard.append(dealcard)
        computerscore=calculatescore(computercard)
    print(f" your final hand: {usercard}, final score: {userscore}")
    print(f" computer's final hand: {computercard}, final score: {computerscore}" )
    print(compare(userscore,computerscore))
while input("do you want to play a game of blackjack? Type 'y' or 'n':").lower=="y":
    playgame()



