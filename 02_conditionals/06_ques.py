distance = input("Enter the Distance: ")
distance = int(distance)

if distance <= 3: 
    print("Walk")
elif distance > 3 and distance < 15:
    print("Bike")
else: 
    print("Car")