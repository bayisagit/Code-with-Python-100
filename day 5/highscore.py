nu=input("enter the integers:").split(",")
for i in range(0,len(nu)):
    nu[i]=int(nu[i])
large=0
for n in nu:
    if n>large:
        large=n
print(f"the highest score in the class is:{large}")
print(nu)
     