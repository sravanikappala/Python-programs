import tkinter as tk
root = tk.Tk()
root.title("example")

l1 = tk.Label(root,text = "num1")
l1.grid(row = 0,column = 0)
l2 = tk.Label(root,text = "num2")
l2.grid(row = 1,column = 0)

e1 = tk.Entry(root)
e1.grid(row = 0,column = 1)
e2 = tk.Entry(root)
e2.grid(row = 1, column = 1)

def add():
    n1 = int(e1.get())
    n2 = int(e2.get())
    r = n1 +n2
    result.config(text = r)
    
    
              
def sub():
    n1 = int(e1.get())
    n2 = int(e2.get())
    r = n1-n2
    result.config(text = r)
    
              
def mul():
    n1 = int(e1.get())
    n2 = int(e2.get())
    r = n1*n2
    result.config(text = r)

def div():
    n1 = int(e1.get())
    n2 = int(e2.get())
    r = n1/n2
    result.config(text = r)
    
              
def power():
    n1 = int(e1.get())
    n2 = int(e2.get())
    r = n1**n2
    result.config(text = r)

def clear():
    e1.delete(0,tk.END)
    e1.insert(0,"")
    e2.delete(0,tk.END)
    e2.insert(0,"")
    result.config(text="")

b1 =tk.Button(root,text = "+" ,width = 10,command = add)
b1.grid(row = 2,column = 0)

b1 = tk.Button(root,text = "-" ,width = 10,command = sub)
b1.grid(row = 2,column = 1)

b1 = tk.Button(root,text = "*" ,width = 10,command = mul)
b1.grid(row = 2,column = 2)

b1 = tk.Button(root,text = "/" ,width = 10,command = div)
b1.grid(row = 3,column = 0)

b1 = tk.Button(root,text = "CE" ,width = 10,command = clear)
b1.grid(row = 3,column = 1)

b1 = tk.Button(root,text = "^" ,width = 10,command = power)
b1.grid(row = 3,column = 2)

result = tk.Label(root,text = "")
result.grid(row = 4, column = 2)

root.mainloop()










































