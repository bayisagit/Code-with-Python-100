worlist=["ardvark","baboon","camel"]
import random
worguest=random.choice(worlist).lower()
print(f"the word guested is {worguest}")
leng=len(worguest)
display=[]
for _ in range(leng):
    display+="-"
print(display)
lives=6
endgame=True
while endgame:
    guess=input("guess the letter:")       
    for position in range(leng):
        letter=worguest[position]
        if letter==guess:
            print(f"you've already guessed {guess}")
            display[position]=letter
        
    if guess not in worguest:
        print(f"you guessed {guess},that's not in the word.you lose a life.")
        lives-=1
        print(" ".join(display))
        if lives==0:
            endgame=False
            print("you lose")
    print(display )
    if "-" not in display:
        endgame=False
        print("you win")


        