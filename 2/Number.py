a = 12 
b = 12
print(a+b)

c = 2.5 
d = 5
print(c*d)

e = 2 ** 100
print(e)

import math
print(math.pi)

import random
print(math.floor(random.random() * 100 + 1))

print(random.choice([1,2,3,4,5]))

# strings

username="hello"
print(len(username))

print(username[0])

print(username[-1])

print(username[1:4])

print(username[1:])
# print(username[0] = 'a') error, as strings are immutable.

print(dir(username))

# list
mylist = [123, "hello", 12.5, True]
print(mylist)
print(len(mylist))
print(mylist[0])
print(mylist[-1])
print(mylist[1:3])
print(mylist[1:])


#  Dictionary
dict1 = {'one': 'hello', 'two': 123, 'three': True}
print(dict1)
print(dict1['one'])
# print(dict1['four']) error, key does not exist
print(dict1.keys())
print(dict1.values())

# Tuple
tup = (123, "hello", 12.5, True)
print(tup)
print(tup[0])
print(tup[1:3])
print(len(tup))
# print(tup[0] = 'a')   error, as tuples are immutable


