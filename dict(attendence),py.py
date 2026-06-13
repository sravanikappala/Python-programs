n = int(input("enter no of students:"))
lt = []
for i in range(n):
    name = input(f"enter name of the {i}student ")
    days = int(input(f"enter no of days present"))
    lt.append((name,days))
print(lt)
dict1 = dict(lt)
print(dict1)
total = 100
for name in dict1:
    days = dict1[name]
    percentage = (days/total)*100
    print(f" for {name} attengence% is {percentage}")

    if percentage <75:
        print(f"{name} is not ")
