fruits = ("apple", "mango","grapes")
print(fruits)
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[-1])
print(fruits[-3])

print(fruits[0:2])
print(fruits[1:])
print(fruits[:2])
# fruits[0]="banana" error, tuples are immutable
# print(fruits)

print(len(fruits))

fruits2 = ("kiwi", "strawberry")
fruits = fruits + fruits2
print(fruits)

if "strawberry" in fruits:
    print("yes")
else:
    print("no")

print(fruits.count("apple"))

print(fruits)
(red, yellow, green, green, red) = fruits
print(yellow)


# ("",(1,2,3),"")