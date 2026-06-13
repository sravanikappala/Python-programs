class Demo:
    def __init__(self,name,marks,age):
        self.nm = name
        self._m = marks
        self.__a = age
    def show(self):
        print("name = ", self.nm)
        print("marks =",self._m)
        print("age :",self.__a)
    def result(self):
        s = self.__a
        if s > 20:
            print("yess")
        else:
            pirnt("noo")



name = input("enter name: ")
marks = int(input("enter marks:"))
age = int(input("enter age:"))
d = Demo(name,marks,age)
d.show()
d.result()

print("in public: ", d.nm)#object use cheysthu elements ni acess cheyadaniki
#d.nm (ekkada nm aneydhi instant variable alaney use cheyali)
print("in protective: ", d._m)
             
