order = input("What would you like to order (Small, Medium, Large)? ")

extra = input("Would you like to add extra espresso (yes, no)? ")

order = order + " coffee"

if extra.lower() == "yes":
    order = order + " with extra espresso"

print(f"Here is your {order}!") 