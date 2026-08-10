# Tuples are immutable

fruits = ("apple", "mango", "cherry")
(fruit1, fruit2, fruit3) = fruits

print(f"Fruits : {fruits}")

ginger, cardamom = 2, 1 # this is possible because of tuple

print(f"ginger: {ginger}, cardamom: {cardamom}")

ginger, cardamom = cardamom, ginger

print(f"ginger: {ginger}, cardamom: {cardamom}")


# membership
print(f"Is pple in fruits? {'apple' in fruits}")