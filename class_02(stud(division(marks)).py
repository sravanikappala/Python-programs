class student:
    clg_nm = "vvitu"
    def __init__(self,ap,sgpa):
        self.attendance = ap
        self.result = sgpa

    def display(self):
        print("attendance percentage:",self.attendance)
        print("result:",self.result)
        print("college:",s.clg_nm)
    def getresult(self):
        s = self.result
        if s >= 90:
            print("distintion")
        elif s >= 80:
            print("2st")
        elif s >= 70:
            print("3rd")
        elif s >= 60:
            print("4th")
        else:
            print("just okkk")

n = int(input("enter no of students"))

for j in range(1,n+1):
    a = float(input("enter attendance percantage"))
    r = float(input("enter result"))          
    s = student(a,r)
    s.clg_nm
    s.display()
    s.getresult()
              
