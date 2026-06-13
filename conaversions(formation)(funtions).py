##def dictionary():
##    lt = []
##    for i in range(n):
##        name = input(f"enter name of {i}")
##        age = int(input(f"enter age of {i}"))
##        lt.append((name,age))
##    print(lt)
##    dict1 = dict(lt)
##    print(dict1)
##    for els in dict1:        
##        age = dict1[els]        
##        if age > 60:
##            print("good")
##        else:
##            print("not ok")
##n = int(input("no of students are:"))
##dictionary()

##def dictionary():
##    lt = []
##    for i in range(n):
##        name = input(f"enter name of {i}")
##        age = int(input(f"enter age of {i}"))
##        lt.append((name,age))
##    print(lt)
##    dict1 = dict(lt)
##    print(dict1)
##    for values in dict1.values():       
##        age = values
##        if age > 60:
##            print(f" {age} good ")
##        else:
##            print(f" {age} not ok ")
##n = int(input("no of students are:"))
##dictionary()

##def student():
##    lt = []
##    for i in range(1,n+1):
##        name = input(f"enter name {i} student")
##        marks = int(input(f"enter ur {i} th marls"))
##        lt.append((name,marks))
##    print(lt)
##    dict1 = dict(lt)
##    print(dict1)
##    marks_list = []
##    for els in dict1:        
##        marks_list.append(dict1[els])
##    print(marks_list)
##    max_mark = max(marks_list)
##    min_mark = min(marks_list)
##    for els in dict1:
##        if dict1[els] == max_mark:
##            print(els)
##n = int(input("no of students"))
##student()
##

def even_sqr():
    d = {}
    for i in lt:
        if i%2 == 0:
            d[i] = i*i
    print(d)
lt = [1,3,7,4,8,9,0]
even_sqr()

#ekkada d[i] anty dictionary[key] ani ardham so direct ga value esthundhi 




        
        
