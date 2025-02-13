age = input('Give me a score value: ')
ageInt = int(age)

if ageInt < 13:
    print("You are a child")
elif ageInt >= 13 and ageInt < 19:
    print("You are a teenager")
elif ageInt >= 19 and ageInt < 59:
    print("You are an adult")   
else: 
    print("You are a senior citizen")
    