def myf(firs,seco):
    if op=='+':
        print(a+b)
    elif op=='-':
        print(a-b)
    elif op=='*':
        print(a*b)
    elif op=='/':
        print(a/b)
    else:
        print("you have entered inappropriate operator!")
a=int(input("enter the first number: "))
op=input("+ - * /")
b=int(input("enter the second number: "))
myf(a,b)