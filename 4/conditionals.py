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