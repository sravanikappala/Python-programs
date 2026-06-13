def cal_bonus(salary,experience):
    if experience > 5:
        return salary*0.20
    else:
        return salary*0.10

def total_amount(salary,bonus):
    return salary+bonus

n = int(input("enter no of employees:"))
for i in range(n):
    print("for employee",i)
    name = input("enter name of the person:")
    salary = int(input("enter salary of the person:"))
    experience = int(input("enter experience:"))
    bonus = cal_bonus(salary,experience)
    total = total_amount(salary,bonus)
    print("name:",name)
    print("bonus:",bonus)
    print("total:",total)
    
    
                 
          
