number = input("Enter a number: ")
number = int(number)

sum = 0
for i in range(1, number):
    if i % 2 == 0:
       sum+=1
print(sum) 