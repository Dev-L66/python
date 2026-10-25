amount = 2
print(f"Initial amount: {amount}")

amount = 12
print(f"Second amount: {amount}")

print(f"ID of 2: {id(2)}")
print(f"ID of 12: {id(12)}")

# numbers are immutable

greetings = set()

print(f"Before adding: {id(greetings)}")

greetings.add("hi")
greetings.add("hello")

print(greetings)
print(f"After adding: {id(greetings)}")

# sets are mutable