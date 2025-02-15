class Car:
    total_car = 0

    def __init__(self, brand, model): 
        self.__brand = brand
        self.model = model
    
    def fuel_type(self):
        return "Petrol or Diesel"

    def full_name(self):
        return (f"{self.__brand} {self.__model}")
    
    @staticmethod
    def general_description(): 
        return "Cars are means of transport"
    
class ElectricCar(Car): 
    def __init__(self, __brand, model, battery_size):
        super().__init__(__brand, model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "Electric Charge"

    
my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
print(my_tesla.fuel_type())

safari = Car("Tata", "Nexon")
print(safari.fuel_type())
print(safari.general_description())