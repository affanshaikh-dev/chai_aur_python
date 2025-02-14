number = 3
for i in range(1, 11):
    if i == 5: 
        continue
    print("{0} x {1} = {2}".format(number, i, number * i))