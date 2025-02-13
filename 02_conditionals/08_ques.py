password = input("Enter Your Password: ")

if len(password) < 6: 
    print("Your are password is weak")
elif len(password) >= 6 and len(password) <= 10:
    print("Your password is Medium")
else: 
    print("Your password is strong")
    