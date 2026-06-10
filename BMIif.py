weight = int(input("enter wt in kg"))
height = float(input("enter ht in cm"))

BMI =round(weight/(height**2))
print(BMI)
if BMI<18.5:
   print("BMI =",BMI,"underweight")
elif BMI<25:
    print(f"{BMI} is normal wt")
elif BMI<30:
    print(f"BMI is{bMI} and overwt")
else:
    print("not valid")

