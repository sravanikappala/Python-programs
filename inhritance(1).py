class person:
    def __init__(self,name,age):
        self.nm = name
        self.ag = age
    def display_p(self):
        print("name is:",self.nm)
        print("age is:",self.ag)
class student(person):
    def __init__(self,name,age,roll,marks):
        super().__init__(name,age)
        self.r = roll
        self.mk = marks
    def display_s(self):
        super().display_p()
        print("rol_number:",self.r)
        print("marks is:",self.mk)

n = int(input("enter no of students:"))
for i in range(1,n+1):
    name = input("enter name:")
    age = int(input("enter age:"))
    roll = int(input("enter rool number:"))
    marks = int(input("entr marks:"))
    p=student(name,age,roll,marks)
#    p.display_p()
    p.display_s()
                     
                    
    
    

  
