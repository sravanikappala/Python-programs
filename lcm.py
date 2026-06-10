a = int(input("enter 1st number: "))
b = int(input("enter 2nd nmber: "))
#maximum = int()
if a>b:
    lcm = a
    
else:
    lcm = b

while (1):
    if lcm%a == 0  and lcm%b == 0:
        print(f"lcm of {a} and {b} is {lcm} ")
        break
    lcm+=1
