# classify age groups: 
# child <13, teen 13-19, 
# adult 20-59, senior 60+

age = int(input("Enter your age: "))  #  whenever we take input from user it is taken as a string, so we convert to int here.

if age < 13:
    print("child")
elif age <= 19:
    print("teen")
elif age <=59:
    print("adult")
else:
    print("senior")


# Movie tickets:
#  $12 foradults, 18 and above
#  $8 for kids
# $2 discount on wednesday

age = 2
price = 12
day ="wdnesday"
price = 12 if age >= 18 else 8
if day == "wednesday":
   price = price -2
print(price)



score = 10

if score > 100:
    print("Invalid scale")
    exit()

if score >= 90:
    grade ="A"
elif score >=80:
    grade = "B"
elif score >= 70:
    grade="C"
elif score >=60:
    grade="D"
else:
    grade="F"
print(grade)
#  ripe checker

fruit = "banna"
color = "yellow"
if fruit == "banana":
  if color == "green":
    print("unripe")
  elif color == "yellow":
    print("ripe")
  elif color == "brown":
    print("overripe")
  else:
    print("unknown color")
else:
  print("unknown fruit")

#    weather checker
weather = "sunny"
if weather == "sunny":
    print("Go to walking.")
elif weather == "Rainy":
   print("Read a book")
elif weather == "snowy":
   print("Build a snowman")


# mode of transportation
distance = 0

if distance < 3:
   print("walk")
elif distance <=15:
   print("bike")
elif distance > 15:
   print("car")

size = "small"
extra_shot = True

if extra_shot:
   coffee = size + " coffee with extra shot"
else:
   coffee = size + "coffee"
   
print(coffee)


#  password strength checker
password = "abc123jriej"
pass_length = len(password)

if (pass_length  < 6):
   print("weak")
elif (pass_length  <10):
   print("medium")
elif (pass_length >= 10):
   print("strong")


# leap year
year = 2024
if (year % 100 != 0 and year % 4 == 0):
   print("leap year")
elif  year % 400 == 0 :
   print("not leap year")

  


   

