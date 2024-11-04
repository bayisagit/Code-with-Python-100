print("welcome to thte rollercoaster!")
height= int(input("what is your height in cm"))
if height>120:
    print("you can ride the rollercoaster!")
    age=int(input("what is your age:"))
    if age<12:
        print("please pay $5.")
    elif age<=18:
        print("please pay $7.")
    else:
        print("please pay $12.")
else:
    print("sorry, you have to grow taller before you can ride.")
print("thank you for your participation!")