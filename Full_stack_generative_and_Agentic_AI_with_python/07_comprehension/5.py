nums = [x for x in range (1,11)]
print(nums)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = [x%2==0 for x in numbers]
print(even)

names = ["john", "sara", "alex", "emma"]
up = [name.upper() for name in names]
print(up)



numbers = [1, 2, 3, 4, 5, 6]
odd = [x**3 if x%2!=0 else x for x in numbers ]

print(odd)


words = ["apple", "cat", "banana", "dog", "orange"]
four = [x for x in words if len(x) > 4]
print(four)


numbers = [10, -5, 20, -3, 0, 8]
negative = [0 if x < 0 else x for x in numbers]
print(negative)


# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
square = {s:s**2 for s in range(1,6)}
print(square)


numbers = [1, 2, 2, 3, 3, 4, 5, 5]

unique = {x for x in numbers}
print(unique)


nums = (x for x in range(1,6))
for n in nums:
    print(n)

even = (x for x in range(1,21) if x%2==0)
print(next(even))
print(next(even))
print(next(even))