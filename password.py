#password = input("enter ur password: ")
#has_upper = False
#has_lower = False
#has_digit = False
#if len(password) >= 8:
#    for ch in password:
#        if ch.isupper():
#       elif ch.islower():
#            has_lower = True
#        elif ch.isdigit():
#            has_digit = True
#if len(password)>=8 and has_upper and has_lower and has_digit:
#    print("strong password")
#else:
#    print("week password")
            
            
email = input("enter ur private email: ")
valid_domine = ['@gmail.com','@college.edu','@yanoo.coin']
if email.count('@') == 1 and ' ' not in email and any(email.endswith(d) for d in valid_domine):
    print("valid eamil")
else:
    print("invalid email")
