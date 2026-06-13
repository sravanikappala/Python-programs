import random
print("selecting any number from range 1 to 100:")
x = random.randint(1,100)
#print(f"the selected number is {x}")
level = input("which level ur preferring easy or hard..???")
if level == 'easy':
    attempts = 10
elif level == 'hard':
    attempts = 5
else:
    print("invalid input")
while (level == 'easy' and attempts >0) or (level == 'hard' and attempts >0):
    guess_num = int(input("enter any number:"))
    if guess_num <x:
       print("you guessed number is too low")
       attempts = attempts-1
       print(f"your left over attempts are {attempts}")
       if attempts == 0:
           print("u had lost game")
    elif guess_num > x:
        print("you guessed number is too high")
        attempts = attempts -1
        print(f" your left over attmpts are {attempts}")
        if attempts == 0:
            print("U had lost game")
    else:
         print("u have won the game")
         break
print(f"the selected number is {x}")

        
     
