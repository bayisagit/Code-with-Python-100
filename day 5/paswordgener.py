import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
large=[char.upper() for char in letters]
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','#','$','%','&','(',')','*','+']
print("welcome to bypassword Generator!")
le=int(input("how many small letters would you like in your password: "))
lle=int(input("how many capital letters would you like in your password: "))
sym=int(input("how many symbols would you like in your password: "))
num=int(input("how many numbers would you like in your password: "))
password=[]
for k in range(0,le):
    password.append(random.choice(letters))
for k in range(0,lle):
    password.append(random.choice(large))
for k in range(0,sym):
    password.append(random.choice(symbols))
for k in range(0,num):
    password.append(random.choice(numbers))
print(password)
random.shuffle(password)
print(password)
passw=""
for u in password:
    passw+=u
print(f"your password is: {passw}")
