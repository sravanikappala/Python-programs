class Demo:
    
    def add(self,a = None,b = None,c = None):
        if a!=None and b!= None and c!= None:
            print(   a + b + c)
        elif a!=None:
            print(a)
        else:
            print(0)
d = Demo()
d.add(5,6,7)
d.add(6)
d.add()


    
