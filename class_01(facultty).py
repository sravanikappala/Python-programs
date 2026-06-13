class faculty:
    def __init__(self,name,course):
         self.nm = name
         self.cs= course
        
    def display(self):
        print("name:",self.nm)
        print("course:",self.cs)
n = int(input("no of faculty:"))
for i in range(n):
    name = input("enter name")
    course = input("enter course")
    f = faculty(name,course)
    f.display()
    
