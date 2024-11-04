for i in range(0,101):
    if i%3==0:
        if i%5==0:
            print("the number is fizzbuzz!")
        else:
            print("the number is fizz!")
    elif i%5==0:
        print("the number is buzz!")
    else:
        print(i)