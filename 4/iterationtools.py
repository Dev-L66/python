import time
print("Hello world")


username = "John Doe"
print(username)


# f = open('iterationtools.py')
# f.readline()
# f.__next__()


for line in open('iterationtools.py'):
    print(line)



f = open('iterationtools.py')
while True:
    line = f.readline()
    if not line: break
    print(line)



test = ""

if not test:
    print("help")



list2 = [1,2,3,4]
I = iter(list2)

print(I) 
I.__next__()


f = open('iterationtools.py')

print(iter(f) is f.__iter__())

print(iter(f) is f)


list1 = [1,2,3,4]
print(iter(list1) is list1)


dict1 = {'a': 1, 'b':1}
for key in dict1.keys():
    print(key)

I = iter(dict1)
# print(I)
# print(next(I))
# print(next(I))
# print(next(I))
# print(next(I))


R = range(0,5)

I = iter(R)
print(I)
print(next(I))
print(next(I))
print(next(I))
print(next(I))
print(next(I))
# print(next(I))

