

while True: 
    number = input("Enter a number (1 to 10): ")
    number = int(number)

    if number >= 1 and number <= 10:
        print("You entered: ", number)
        break
    else: 
        print("Invalid number. Try again.")
        continue
