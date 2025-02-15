file = open('youtube.txt', 'w')

try: 
    file.write("Chai Aur Code")
finally:
    file.close()

with open('youtube.txt', "w") as file:
    file.write("chai aur python")