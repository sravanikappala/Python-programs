#public acessing
class A:
    def __init__(self):        
        self.x = 10
    def display(self):
        print("value of x :",self.x)

class B:
    def show(self):
        obj = A()
        print(obj.x)
        obj.display()
b = B()
b.show()


#protective acessing

class A:
    def __init__(self):        
        self._x = 10
    def _display(self):
        print("value of x :",self._x)

class B:
    def show(self):
        obj = A()
        print(obj._x)
        obj._display()
b = B()
b.show()



#private acessing
class A:
    def __init__(self):        
        self.__x = 10
    def display(self):
        print("value of x :",self.__x)

a = A()
a.display()
