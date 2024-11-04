import random
nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
ju=random.choice(nums)
print("welcome to the number guessing game")
print("I am thinking of a number between 1 and 30 includes")
ch=input("choose a difficulty. Type 'easy' or 'hard': ").lower()
if ch=="hard":
    isrealgus=True
    remain=5
    while isrealgus:
        print(f"you have {remain} remaining to guess the number.")
        gu=int(input("make a gus: "))
        if gu>ju:
            print("too high")
            print("guess again.")
        elif gu<ju:
            print("too low")
            print("guess again.")
        elif gu==ju:
            print(f"you got it! the answer was {ju}")
            isrealgus=False
        remain-=1
        if remain==0:
            isrealgus=False
            print("you lose it you are out of the game")
elif ch=="easy":
    isrealgus=True
    remain=10
    while isrealgus:
        print(f"you have {remain} remaining to guess the number.")
        gu=int(input("make a gus: "))
        if gu>ju:
            print("too high")
            print("guess again.")
        elif gu<ju:
            print("too low")
            print("guess again.")
        elif gu==ju:
            print(f"you got it! the answer was {ju}")
            isrealgus=False
        remain-=1
        if remain==0:
            isrealgus=False
            print("you lose it you are out of the game")





