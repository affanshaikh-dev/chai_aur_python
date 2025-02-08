# this is for importing the module of number
import math
# math.floor(2.9) # 2
# math.ceil(2.2) # 3
# math.sqrt(16) # 4.0
# math.pow(2,3) # 8.0
# math.pi # 3.141592653589793
# math.e # 2.718281828459045
# math.trunc(2.9) # 2

# random numbers
# import random
# random.random() # random numbers limit: 0.0 <= x < 1.0
# random.randint(1, 20) # random numbers limit: 1 <= x <= 20
# random.choice([1, 2, 3, 4, 5]) # random numbers limit: 1 <= x <= 5
# random.shuffle([1, 2, 3, 4, 5]) # random numbers limit: 1 <= x <= 5

# complex numbers
# print(1  + 1j) # (1+1j)
# print((1  + 1j)* 5)  # (5+5j)

# octal numbers
# print(0o123) # 83
# print(oct(83)) # 0o123

# hexadecimal numbers
# print(0xff) # 255
# print(hex(255)) # 0xff

# binary numbers
# print(0b1010) # 10  
# print(bin(10)) # 0b1010

# integer coversion
# print(int(3.14)) # 3
# print(int("64", 8)) # 52
# print(int("64", 16)) # 100
# print(int("10000", 2)) # 16

# decimal numbers
# from decimal import Decimal
# print(Decimal("0.1") + Decimal("0.1") + Decimal("0.1") - Decimal("0.3")) # Decimal('0.0')  

# fractions
# from fractions import Fraction
# myFra = Fraction(2, 7)
# print(myFra)

# set numbers
setone = {1, 2, 3, 4, 5}
setone & {1 , 2, 3} # intersection of two sets
setone | {1 , 2, 3} # union of two sets
print(setone - {1 , 2, 3, 4, 5}) # difference of two sets
print(type(setone))