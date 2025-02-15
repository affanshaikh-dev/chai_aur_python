class Car:
    total_car = 0

    def __init__(self, brand, model): 
        self.__brand = brand
        self.__model = model

    def full_name(self):
        return (f"{self.__brand} {self.__model}")
    
    @property
    def model(self):
        return self.__model

nexon = Car("Tata", "Nexon")
# safari.model = "city"

print(nexon.model)