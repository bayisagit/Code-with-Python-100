import random
nam=input("give me a everybody name,seperated by a comma.")
na=nam.split(",")
print(na)
print(na[0])
dh=len(na)
print(dh)
ra=random.randint(0,dh-1)
per=na[ra]
print(per+" is going to buy the meal!")