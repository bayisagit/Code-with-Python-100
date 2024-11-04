print("WELL COME TO THE TIP CALCULATOR!!")
print(".....................................")
print(".....................................")
print(".....................................")
bill=float(input("what was the total bill:"))
perc=int(input("what percentage tip would you like to give:"))
peop=int(input("how many people to split tht bill:"))
div=perc/100
cul=div*bill
com=cul+bill
result=com/peop
col=round(result,2)
num="{:.2f}".format(result)
print(f"each person should pay {col}!")
print(f"each person should pay {num}!")
