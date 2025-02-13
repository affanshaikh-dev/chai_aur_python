species = input("Enter the species: ")
age = input("Enter the age: ")

if species.lower() == "cat":
    if int(age) < 8:
        print("Kitten Food")
    else:
        print("Adult Food")
elif species.lower() == "dog":
    if int(age) < 10:
        print("Puppy Food")
    else:
        print("Adult Food")
else: 
    print("Unknown species")

