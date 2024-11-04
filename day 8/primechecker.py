def che(n):
    pr=True
    for i in range(2,n):
        if n%i==0:
            pr=False
    if pr:
        print("the number is prime!")
    else:
        print("the number is not prime!")
n=int(input("enter the number:"))
che(n)