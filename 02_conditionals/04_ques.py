fruit = "banana"
fruitColor = input("Enter the color of the fruit (Green, Yellow, Brown): ")

print("===== ", fruit, " =====")
if fruitColor == "Green":
    print("The",  fruit ," are Unripe")
elif fruitColor == "Yellow":
    print("The", fruit," Fruit are Ripe")
elif fruitColor == "Brown": 
    print("The", fruit ,"are Overripe")
else:
    print("Enter Valid Input")