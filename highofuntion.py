from functools import reduce
n = int(input("enter no of digits:"))
lt = []
for i in range(n):
    num = int(input("enter number:"))
    lt.append(num)
print(lt)

squares = list(map(lambda x:x**2,lt))
evens = list(filter(lambda x: x%2 == 0,lt))
total_se = reduce(lambda x,y:x+y,lt)
print("squares:",squares)
print("even number:",evens)
print("total:",total_se)







