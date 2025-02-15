class Car:
    def __init__(self, brand, model): 
        self.__brand = brand
        self.model = model
    
    def full_name(self):
        return (f"{self.__brand} {self.__model}")

class Battery: 
    def battery_info(self):
        return "This is battery"

class Engine:
    def engine_info(self):
        return "This is Engine"

class ElectricCar(Battery, Engine, Car):
    pass

new_tesla = ElectricCar("Tesla", "Model S")
print(new_tesla.engine_info())
print(new_tesla.battery_info())