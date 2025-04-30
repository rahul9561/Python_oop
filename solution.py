class Car:
    car_num_count=0

    def __init__(self,brand,color):
        self.__brand = brand
        self.__color = color
        Car.car_num_count += 1  # Increment the car number count for each new instance

    def get_brand(self):
        return self.__brand

    def full_name(self):
        return f"{self.__brand} {self.__color}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def get_descriptions():
        return "this is a car"
    
    @property
    def get_color(self):
        return self.__color



c1=Car("Toyota", "Blue")
# c1.color = "green" 
# print(c1.color)
# print(c1.full_name()) # Attempting to change the private attribute directly (not recommended)
# print(c1.get_color)
# c2=Car("brizza", "gray")
# print(c1.get_descriptions())  # Accessing the private attribute using the getter method
# print(Car.get_descriptions())
# print(c1.get_brand())  # Accessing the private attribute using the getter method
# print(c1.color)
# print(c1.full_name())  # Accessing the private attribute using the getter method
# print(c1.fuel_type()) 
# print(Car.car_num_count) # Accessing the private attribute using the getter method

# print(c1.full_name())


class ElectricCar(Car):
    def __init__(self, brand, color):
        super().__init__(brand, color)  # Call the constructor of the parent class
        self.battery = "100kWh"
        self.range = "300 miles"

    def fuel_type(self):
        return "elecric charge"






ec1=ElectricCar("Tesla", "Red")

# print(isinstance(ec1, Car))  # Check if ec1 is an instance of the Car class
# print(isinstance(ec1,ElectricCar))
# print(ec1.fuel_type())

# print("function call=",ec1.full_name())





# multiple inheritance
class Battery:
    def batt(self):
        return "Battery class initialized"
class Engine:
    def eng(self):
        return "Engine class initialized"


class ElectricCarWithBattery(Battery , Engine):
    pass

ec3=ElectricCarWithBattery()
print(ec3.batt())
print(ec3.eng())
