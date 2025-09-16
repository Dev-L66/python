x = 1
y = 2
z = 3
print(x+y)
print(x+y*z)
print((x +  y) * z)
print(40 + 2.23)
print('40' + '2.23')
# print(40 + 'str') error 
print('hello' + ' ' + 'world')
print(x,y,z)

print(y%2)
print(z ** 2)
# print(2 ** 10000)

result = 1/3.0
print(result)



print(repr('hello\nworld'))
print(str('hello\nworld'))
print('hello\nworld')


print( 1 < 2)
print( 1 > 2)
print( 2.0 == 2)
print( 1 != 2)
# x 1, y 2, z 3
print(x<y<z)

print( 1 == 2 < 3)
import math
# floor - round to lower
print(math.floor(3.5))
print(math.floor(3.9))
print(math.floor(-3.5))

# trunc - towards zero
print(math.trunc(3.5))
print(math.trunc(-2.8))

# complex
print(2+ 1j)
print((2 + 1j) * 6)


# 
print(0o20)
print(0xFF)
print(0b100)
print(oct(64))
print(hex(64))
print(bin(64))
print(int(2.3))
print(int('64', 8))
print(float(2))

x = 10
print(x >> 2)


import random
print(random.randint(1, 10))
print(random.choice([1,2,3,4,5]))
list1 = [1,2,3,4,5]
random.shuffle(list1)
print(list1)


print(0.1 + 0.1 + 0.1 - 0.3)

# precision with decimals and fractions
from decimal import Decimal

print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))


from fractions import Fraction
myFra = Fraction(2,6)
print(myFra)


# set

set1 = {1,2,3,4}
print(set1 & {1,3})
print(set1 | {1,3})

print(set1-{1,2,3,4})

print(type({}))
print(type(True))
print(True == 1)
print(False == 0)
print(True is 1)
