vechicle = input("enter type of vechicle t/c/bike")
hours = int(input("enter no.of hours"))
if vechicle == "t":
    charge = 20*hours
    print(charge)
elif vechicle == "c":
    charge = 15*hours
    print(charge)
elif vechicle == "bike":
    charge = 10*hours
    print(charge)
else:
    print("invalid vechicle")
