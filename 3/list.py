fruits = ["apple", "mango","grapes"]
print(fruits)
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[-1])
print(fruits[-2])
print(fruits[-3])

print(fruits[0:2])
print(fruits[1:])
print(fruits[:2])

fruits[0] = "banana"
print(fruits)

print(fruits[1:2])
fruits[1:2] = "orange"
print(fruits)
fruits = ["apple", "mango","grapes"]
fruits[1:2] = ["orange"]
print(fruits)

