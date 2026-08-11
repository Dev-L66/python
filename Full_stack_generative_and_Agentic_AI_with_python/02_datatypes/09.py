# set - has unique values

fruits = {"apple", "orange", "mango"}
fruits_1 = {"cherry", "apple", "strawberry"}


# union | - all from both sets but dont repeat the common value
all_fruits = fruits | fruits_1

print(f"All fruits: {all_fruits}")


# intersection & - common from both set
all_fruits = fruits & fruits_1
print(f"Common spices {all_fruits}")


#  only in fruits
only_in_fruits = fruits - fruits_1
print(f"Common spices {only_in_fruits}")


print(f"Is apple in fruits?{'apple' in fruits}")


