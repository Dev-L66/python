#  Object and mutability
# Everything in python is an object
# Every object has identity
# Every object has a type
# Every object has a value
# mutable (can be changed) and immutable (cannot be changed)
# mutability depends on identity and not value


sugar_amount = 2
print(f"Initial sugar: {sugar_amount}")

sugar_amount = 12
print(f"Initial sugar: {sugar_amount}")

# reference is changed
print(f"ID of 2: {id(2)}")
print(f"ID of 12: {id(12)}")