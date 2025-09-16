a = """hello"""
b ="hello"
c = 'hello'

first_char = a[0]
print(first_char)
print(a[0:4])
print(a[0:-1])
print(a[:])
print(a[:4])
print(a[0:5:4])
print(a[0:5:-1])

name = "   Serah Alex    "
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.strip()) # removes spaces from start and end   
# print(name) will not change as string is immutable
print(name.replace("Serah", "Hune"))
print(name)

words = "Hello world, what's going on?"
print(words.split(","))
print(words.find("world"))
print(words.find("hello"))
print(words.count("Hello"))
print(words.count("hello"))



e = 6
f = 66

order = "I have {} apples and {} oranges."
print(order.format(e, f))

fruits = ["apple", "mango", "orange"]
print(fruits)
print(", ".join(fruits))

d = "hello"
print(len(d))

for letter in d:
    print("..",letter)


weather = "The weather is \"sunny\"."
print(weather)

p = "I'm\nawesome"
print(p)

q = r"I'm\nawesome"
print(q)

print("real" in q)
print("awesome" in q)