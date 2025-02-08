tea_varities = ["Black", "Green", "White", "Herbal"]
# print(tea_varities[0:3]) # slicing the list
# print(tea_varities)

# tea_varities[3] = "Oolong Tea" 
# print(tea_varities)

# tea_varities[1:2] = ["Lemon"]
# print(tea_varities)

# tea_varities[1:3] = ["Lemon", "Green"]
# print(tea_varities)

# print(tea_varities[1:1])

# loops and conditionals in list
# for tea in tea_varities:
#     print(tea, end = "-")

# append in list
tea_varities.append("Oolong")

# if "Oolong" in tea_varities:
#     print("Yes, Oolong is there")

# pop in list
tea_varities.pop()
# print(tea_varities) # to remove the last element

# remove in list
tea_varities.remove("Green")
# print(tea_varities)

# insert in list
tea_varities.insert(1, "Green")
# print(tea_varities)

# extend in list
tea_varities.extend(["Oolong", "Chamomile"])
# print(tea_varities)

# copy in list
tea_varities_copy = tea_varities.copy() 
# print(tea_varities_copy)

# clear in list
tea_varities_copy.clear()
# print(tea_varities_copy)

# squared number in list
square_num = [i**2 for i in range(1, 11)]
# print(square_num)