#lt1 = [1,2,2,3,3,4,5,4,6,1]
#lt2 =[]
#for i in lt1:
#    if i not in lt2:
#        lt2.append(i)
#print(lt2)    







#lt = [1,3,3,4,5,6,2,3,4,4,5]
#visited = []
#for i in lt:
#    if i not in visited:
#        print(lt.count(i))
#        visited.append(i)
#print(visited)        
   
#lt = [1,2,3,1,2,2,3,4,5,6,7]
#rlt = []
#c = 0
#for i in lt:
#    if i  not in rlt:
#       if lt.count(i) == 1:
#            c+=1
#print(c)                

lt = [ 1,2,1,3,9,0,0,5,0,0,7,0]
zeroes = []
non_zeroes = []
for i in lt:
    if i == 0:
        zeroes.append(i)
    else:
        non_zeroes.append(i)
print(non_zeroes+zeroes)

