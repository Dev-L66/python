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
print(fruits[1:1])
fruits[1:1] = ["strawberry", "strawberry"]
print(fruits)
print(fruits[1:3])
fruits[1:3] = []
print(fruits)


for fruit in fruits:
    print(fruit)

if "apple" in fruits:
    print("yes")
else:
    print("no")

fruits.append("kiwi")
print(fruits)
print(fruits.pop())
print(fruits.pop(2))
fruits.remove("apple")
print(fruits)

fruits.insert(1, "grapes")
fruits.insert(3, "pomegrante")
print(fruits)


fruits_copy = fruits.copy() # shallow copy, new reference is created

fruits_copy2 = fruits # deep copy, same reference 

print(fruits)
print(fruits_copy)
print(fruits_copy2)

fruits.insert(5,"mango")
print(fruits)
print(fruits_copy)
print(fruits_copy2)


print(range(10))
y = range(10)
print(y)
squared_nums = [x**2 for x in range(10)]
print(squared_nums)