print("welcome to python pizza deliveries!")
bill=0
size=(input("what is the size pizza do you want: S for small,M for medium,L for large."))
ad=input("do you want peproni:")
ex=input("do you want extra cheese:")
if size=="S":
    bill+=15
elif size=="M":
    bill+=20
elif size=="L":
    bill+=25
if ad=="y":
    if size=="s":
        bill+=2
    else:
        bill+=3
if ex=="y":
    bill+=1
print(f"your final bill is {bill}")
        