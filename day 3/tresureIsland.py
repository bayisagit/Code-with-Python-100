print("welcome to treasure island.")
print(".....................................")
print(".....................................")
print(".....................................")

print("your mission is to find the treasure.")
c=input("you are at a crossread,would you want to go left or right: if right print R and if left print L ")
if c=="r":
    print("game over!")
else:
    c1=input("you have to come to a lake,swim or wait: S for swim and W for wait ")
    if c1=="s":
        print("game over!")
    else:
        c2=input("you have to come a door,wich door you want enter:enter R for red,B for blue and Y for yellow ")
        if (c2=="r") or (c2=="b"):
            print("game over!")
        else:
            print("congra you win!")