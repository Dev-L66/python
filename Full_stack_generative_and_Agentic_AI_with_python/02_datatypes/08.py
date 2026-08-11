# mutable data types - lists, 

fruits = ["apple", "mango"]

fruits.append("watermelon")
print(f"Fruits: {fruits}")

fruits.remove("watermelon")
print(f"Fruits: {fruits}")

names = ["Alex", "Sara", "Hala"]
roll_no = ["1","2","3"]

names.extend(roll_no)

print(names)

names.insert(2, "George")   # inserts at position 2

print(names)

last = names.pop()

print(last)

print(names)

names.reverse()
print(names)

names.sort()
print(names)

sugar = [1,2,3,4,5]
print(f"Max sugar level {max(sugar)}")
print(f"Min sugar level {min(sugar)}")


# Operator overloading
drink = ["water", "milk"]
flavour = ["ginger"]

mix = drink + flavour
print(mix)

brew = ["black tea", "water"] * 3
print(brew)

player = bytearray(b"Ronaldo")
player = player.replace(b"Rona", b"Cristiano" )
print(f"Bytes: {player}")

