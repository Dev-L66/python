#  basic syntax

def squared_num(n):
    return n ** 2


result = squared_num(2)
print(result)

# sum of parameters, take 2 parameters

def summ(a,b):
    return a + b

res = summ(6,7)
print(res)


# polymorphism in funcs, multiply 2 numbers but also strings

def mul(a,b):
    return a * b
print(mul(6,7))
print(mul(6,"b"))


# return both area and circumference when radius is given
import math

def circle(radius):
    area = math.floor(math.pi * radius ** 2)
    circumference = math.floor(2 * math.pi * radius)
    return area, circumference

a, b = circle(3)
print(a, b)


# default parameter

def greeting(name="John"):
   return f"Good morning {name}"

print(greeting())
print(greeting("Doe"))


#  lambda func to calculate cube

cube = lambda x: x ** 3

print(cube(3))

# func with *args

def add(*args):
    print(*args)
    print(args)
    return sum(args)


print(add(1,2,3,4))


# def add(*hello):
#     return sum(hello)


# print(add(1,2,3,4))


# func with *kwargs
def print_kwargs(**kwargs):
   for key, value in kwargs.items():
      print(key, value)

print_kwargs(name="superman", power="lazer")
print_kwargs(power="lazer",name="superman")
print_kwargs(power="lazer",name="superman", weakness="kryptonite")


# generate func with yield

def even(limit):
    for i in range(2,limit+1,2):
        yield i

for num in even(10):
    print(num)


#  recurrsive func to calculate factorial
def factorial(n):
    if n == 0:
        return 1
    else:
       return n * factorial(n-1)
    
print(factorial(5))