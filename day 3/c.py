hei=float(input("what is your height in m:"))
we=float(input("what is your weight:"))
bmi=round(we/hei**2,2)
if bmi<18.5:
    print(f"your bmi is {bmi}, you are under weight!")
elif bmi<25:
    print(f"your bmi is {bmi}, you are a normal weight!")
elif bmi<30:
    print(f"your bmi is {bmi}, your are overweight.")
elif bmi<35:
    print(f"your body mass is {bmi}, you are obese!")
else:
    print(f"your bmi is {bmi}, you are clinically obese!")
