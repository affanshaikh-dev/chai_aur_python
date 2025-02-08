tea_types = ('green', 'black', 'herbal')
# print(tea_types[-2])

# tea_types[0] = "oolong" # TypeError: 'tuple' object does not support item assignment
more_tea = ('oolong', 'white')
# print(tea_types + more_tea)

# if 'green' in tea_types:
#     print('Yes, we have green tea')

(black, green, herbal) = tea_types
print(green)
