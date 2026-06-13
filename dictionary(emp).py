n = int(input("enter no of employess  in office :"))
lt = []
for i in range(n):
    emp_id = input("enter id :")
    name = input("enter name of person")
    dept = input("enter department belongs to:")
    salary = float(input("enter salary:"))
    lt.append((emp_id,(name,dept,salary)))
print(lt)
dict1 = dict(lt)
print(dict1)
salary_list = []

for emp_id in dict1:
    salary_list.append(dict1[emp_id][2])
    
max_salary = max(salary_list)
min_salary = min(salary_list)
print("high: ",max_salary)
print("lowest: ",min_salary)

for emp_id in dict1:
    if dict1[emp_id][2] == max_salary:
        print("employee with highest salary : ",dict1[emp_id])
        
