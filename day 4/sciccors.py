import random
ch=int(input("what do you want choose: type 0 for rock,1 for paper or 2 for scissors."))
com=random.randint(0,2)
print(com)
if com==0 and ch==2:
    print(f"the computer choose {com} you lose!")
elif com==0 and ch==1:
    print(f"the computer choose {com} you win!")
elif com==1 and ch==0:
    print(f"the computer choose {com} you lose!")
elif com==1 and ch==2:
    print(f"the computer choose {com} you win!")
elif com==2 and ch==0:
    print(f"the computer choose {com} you win!")
elif com==2 and ch==1:
    print(f"the computer choose {com} you lose!")
elif com==ch:
    print("it is draw")
else:
    print("you entered invalid number!")