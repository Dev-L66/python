#  create car class with brand and model as attributes
# create instance of this class

class Car:
    total_cr = 0
    def __init__(self,brand, model):
     self.__brand = brand
     self.__model = model
     Car.total_cr += 1

     # encapsulate
    def get_brand(self):
        return self.__brand
    #  method to display fullname 
    def fullName(self):
       print(f"The model of the car is {self.__model} and the brand is {self.get_brand()}.")
    def fuel_type(self):
       return "Petrol or Diesel"
    @staticmethod
    def general_description():
     return "This is a car"
    @property
    def model(self):
       return self.__model
    
# self is used to link instance to class
# object is an instance of a class  

# inherit from car class - electric class
class ElectricCar (Car):
   def __init__(self, brand, model, battery_size):
      super().__init__(brand, model)
      self.battery_size = battery_size
   def fuel_type(self):
       return "Electric charge"
   
my_car = Car("Toyota", "Corolla")
print(my_car)
print(my_car.get_brand(), my_car.model)
print(my_car.fuel_type())


my_car2= Car("Honda", "Civic")
print(my_car2.get_brand(), my_car2.model)

my_car.fullName()
my_car2.fullName()


my_tesla = ElectricCar("Tesla","Model S","")
print(my_tesla.get_brand(), my_tesla.model, my_tesla.battery_size)
my_tesla.fullName()

# polymorphism
print(my_tesla.get_brand())
print(my_tesla.fuel_type())

# no of cars creatd
print(my_car.total_cr)
print(Car.total_cr)
# print(my_car.general_description()) error, as static method cannot be called on instance
# no need for self in static method
print(Car.general_description())
 
# print(my_car.model()) error , when using property you cannot use () also yu cannot update the value
# my_car.model ="Camry"
print(my_car.model)

#  to check if object is instance of class 

print(isinstance (my_tesla, Car))
print(isinstance (my_tesla, ElectricCar))

print(isinstance (my_car, Car))
print(isinstance (my_car, ElectricCar))

print(issubclass(ElectricCar, Car))
print(issubclass(Car, ElectricCar))



# multiple inheritance
class Battery:
   def battery_info(self):
      return "this is a battery"
   pass

class Engine:
   def engine_info(self):
      return "this is an engine"

class ElectricCar(Battery, Engine):
   pass


my_new_tesla = ElectricCar()
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())