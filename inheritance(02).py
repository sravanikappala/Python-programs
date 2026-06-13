class shape:
    def area(self):
        print("area no defined")
class rectangle:
    def __init__(self,length,breadth):
        self.len = length
        self.brea = breadth
    def area1(self):
        result1 = self.len * self.brea
        print(" area of rectangle :",result1)
class circle:
    def __init__(self,radius):
        self.rad = radius
    def area2(self):
        result2 = 3.14*self.rad**self.rad
        print("area of circle :",result2)                                                    

l = int(input("enter lenth:"))
b = int(input("enter breadth:"))
R = int(input("enter rdius:"))
r = rectangle(l,b)
r.area1()
c = circle(R)
c.area2()
