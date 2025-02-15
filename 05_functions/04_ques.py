import math
def circle_stats(radius): 
    area = math.pi * radius ** 2
    cirumference = 2 * math.pi * radius
    return area, cirumference

a, c = circle_stats(10)
print(f"Area: {a:.2f}, Circumference: {c:.2f}")  