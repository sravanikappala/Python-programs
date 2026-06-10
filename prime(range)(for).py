#for i in range(2,51):
#    for j in range(2,i):
#        if i%j == 0:
#            break
#    else:
#            print(i)
        
            


#f = 1
#for i in range(1,6):
#    f =f*i
#print(f)

#for i in range(1,6):
#    for j in range(1,11):
#        print(f"{i} x {j} ={i*j}")
#        


#s = input("enter strings")
#l_w = s.lower()
#c = 0
#vowels = "aeiou"
#for i in l_w:
#    if i in vowels:
#        print(i)
#        c+=1
#print(c)        

num = input("enter 7 numbers")
num_list = num.split(" ")
print(num_list)
for i in range(len(num_list)):
    num_list[i] = int(num_list[i])
    
for i in num_list:
    if i%3==0:
        continue
    print(i)
