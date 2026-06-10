import random
names = input("enter names seperated by spaces")
names_list = names.split(" ")
person_selection = random.randint(0,length)
print(person_selection)
s = names_list[person_selection]
print(f"{s} will pay the bill")



selection = random.randint(0,2)
print(selection)
if selection == 0:
    print("heads")
else:
    print("tails")
    
