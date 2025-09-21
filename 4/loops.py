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


# repetitive char in a str
word = "helloo"


for char in word:
   if word.count(char) == 1:
      print(char)
      break

# factorial using while loop
num = 5
factorial = 1
while num > 0:
   factorial = factorial * num
   num = num - 1 
print(f"Factorila of {n} is {factorial}")



#  validate inpt

while True:
 number = int(input("Enter value btw 1-10"))
 if 1<= number <= 10:
    print("Thanks")
    break
 else:
   print("Invalid number try again!")


   #  prime number checker

number = 3
isPrime = True

if number > 1:
   for i in range(2, number):
      if (number % i) == 0:
         isPrime = False
         break
print(isPrime)



#  duplicate checker

items = ["apple", "banana", "mango", "apple", "orange"]

unique_items = set()
for item in items:
   if item in unique_items:
      print("Duplicate", item)
      break
   unique_items.add(item)
print(unique_items)



# exponential backoff
import time

wait_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
   print("Attempts",attempts, "wait time", wait_time)
   time.sleep(wait_time)
   wait_time *= 2
   attempts += 1
