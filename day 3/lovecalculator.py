print("welcome to the love calculator!")
nam1=input("what is your name:\n")
nam2=input("what is their name:\n")
su=nam1+nam2
sm=su.lower()
t=sm.count("t")
r=sm.count("r")
u=sm.count("u")
e=sm.count("e")
fi=t+r+u+e
l=sm.count("l")
o=sm.count("o")
v=sm.count("v")
e=sm.count("e")
la=l+o+v+e
las=int(str(fi)+str(la))
if (las<10) or (las>90):
    print(f"your score is {las}, you go together like coke and mentos.")
elif (las>=40) and (las<=50):
    print(f"your score is {las}, you are alright together!")
else:
    print(f"your score is {las}.")