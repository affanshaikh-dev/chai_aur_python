chai_types = {"Masala": "Spicy", "Ginger": "Zesty", "Green":"Mild"}
# print(chai_types["Masala"])

# update values in dictionary
chai_types["Green"]="Fresh"
# print(chai_types)

# method in dictionary
#get method
chai_types.get("Ginger")

#update method
chai_types.update({"Green":"Mild"})
# print(chai_types)

# append method
chai_types["Black"]="Strong"
# print(chai_types)

# pop method
chai_types.pop("Black")
# print(chai_types)

# popitem method
chai_types.popitem()
# print(chai_types)

# del method
chai_types["Black"]="Strong"

# copy method
chai_types_copy = chai_types.copy()
# print(chai_types_copy)  

# itration in dictionary
# for chai in chai_types:
#     print(chai, chai_types[chai])

# for key, values in chai_types.items():
#     print(key, values)

# condition in dictionary
# if "Masala" in chai_types:
#     print("Yes, Masala is in the dictionary")


# multiple dictionary
tea_shop = {
    "Chai": {
        "Masala": "Spicy",
        "Ginger": "Zesty",
        "Green":"Mild"
    },
    "Coffee": {
        "Black": "Strong",
        "Latte": "Mild",
        "Cappuccino": "Medium"
    }
}

# print(tea_shop["Chai"]["Ginger"])


squared_num = {x:x**2 for x in range(10)}
squared_num.clear()
# print(squared_num)

keys = ["Masala", "Ginger", "Lemon"]
values = ["Spicy", "Zesty", "Sour"]
# default_value = "Mild"

# chai_types = dict.fromkeys(keys, default_value)
chai_types = dict(zip(keys, values))

print(chai_types)