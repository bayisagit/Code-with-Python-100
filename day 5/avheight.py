sthe=input("input a list of student height:").split(",")
for n in range(0,len(sthe)):
    sthe[n]=int(sthe[n])
print(sthe)
to=sum(sthe)
num=len(sthe)
av=to/num
print(f"the average height is {av}")