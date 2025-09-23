#  create car class with brand and model as attributes
# create instance of this class

class Car:
    def __init__(self,brand, model):
     self.brand = brand
     self.model = model
    #  method to display fullname 
    def fullName(self):
       print(f"The model of the car is {self.model} and the brand is {self.brand}.")
    

class ElectricCar (Car):
   def __init__(self, brand, model, battery_size):
      super().__init__(brand, model)
      self.battery_size = battery_size
my_car = Car("Toyota", "Corolla")
print(my_car.brand, my_car.model)

my_car2= Car("Honda", "Civic")
print(my_car2.brand, my_car2.model)

my_car.fullName()
my_car2.fullName()

# inherit from car class - electric class



my_tesla = ElectricCar("Tesla","Model S","")
print(my_tesla.brand, my_tesla.model, my_tesla.battery_size)