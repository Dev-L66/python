# count positive numbers
numbers = [-1,2,3,4,5,-6,-7]
count = 0

for number in numbers:
    if number > 0:
     count = count + 1

print(count)

#  sum of even nummbers 
count= 0
even_numbers = [1,2,3,4,5,6,7]
for num in even_numbers:
   if num % 2 == 0:
      count = num + count

print(count)



#  
n = 10
sum_even = 0

for i in range(1, n+1):
   if i % 2 == 0:
      sum_even = sum_even + 1

print(sum_even)

# print table of a number till 10
a = 7
for i in range(1, 11):
   if i == 5:
      continue
   else:
    print(f"{i} x = {i * a}")
 

#   reverse a string
original_str = "hello"
reversed_str = ""


for char in original_str:
   reversed_str =  char + reversed_str 

print(reversed_str)
