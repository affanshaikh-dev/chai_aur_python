class Car:
    def __init__(self, brand, model): 
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + "' "

    def set_brand(self, brand):
        self.__brand = brand
    
    def full_name(self):
        return (f"{self.__brand} {self.__model}")
    
class ElectricCar(Car): 
    def __init__(self, __brand, model, battery_size):
        super().__init__(__brand, model)
        self.battery_size = battery_size

    
my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

my_tesla.set_brand("TeslA")
print(my_tesla.get_brand())