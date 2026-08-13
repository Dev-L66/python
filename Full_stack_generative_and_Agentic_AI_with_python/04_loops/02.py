# looping through lists
fruits = ["apple", "mango", "orange"]

for fruit in fruits:
    print(fruit)


# enumerate - to print list with index number
veggies = ["cucumber", "tomato", "potato"]

for veg in veggies:
    print(f"Veggies: {veg}")

for index, item in enumerate(veggies, start=1):
    print(index, item)

