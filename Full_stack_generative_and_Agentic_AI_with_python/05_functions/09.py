# name = "Alex"

# def greeting(name):
#     print("Hello", name)


# greeting(name)
# print(name)


names = [1,2,3]

def edit_names(rollno):
    rollno[1] = 43

edit_names(names)
print(names) 


def make_chai(tea, milk, sugar):
     print(tea, milk, sugar)


make_chai("Ginger", "Yes", "Low") # positional arguments
make_chai(tea="Milk", sugar="Medium", milk="Yes") # keywords

# (*args, **kwargs)
def special_chai(*ingredients, **extras):
     print("Ingredients", ingredients)
     print("Extras", extras)

# *kwargs
special_chai("Cinnamon", "Cardomom", sweetner="honey", foam="yes")


def hello(name="Haland"):
     print("Hello", name)


hello()


# def chai_order(order=[]):
#      order.append("Ginger")
#      print(order)

def chai_order(order=None):
     if order is None:
        order =[]
     print(order)
     

chai_order()
chai_order()