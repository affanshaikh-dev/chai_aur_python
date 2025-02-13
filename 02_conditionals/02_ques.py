age = input("Enter you Age: ")
age = int(age)

#rates 
adults = 12
childrens = 8

day = input("""Enter the day: \n
            1. Monday\n
            2. Tuesday\n
            3. Wednesday\n
            4. Thursday\n
            5. Friday\n
            6. Saturday\n
            7. Sunday\n""")
day = int(day)

if(age<18):
    if(day == 3):
        print("Movie Ticket Price is:", adults/2)
    else:
        print("Movie Ticket Price is:", adults)
else:
    if(day == 3):
        print("Movie Ticket Price is:", childrens/2)
    else:
        print("Movie Ticket Price is:", childrens)