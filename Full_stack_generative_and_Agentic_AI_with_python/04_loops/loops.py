# for number in range(1, 11):
#     print(f"The number is: {number}")

# for order in range(1, 5):
#     print(f"Preparing order {order}")

# colors = ["red", "green", "blue"]

# for color in colors:
#     print(f"The color is: {color}")


# colors = ["red", "green", "blue"]
# n = list(enumerate(colors))
# print(n)

# for color in colors:
#     print(f"The color is : {color}")

# for idx, item in enumerate(colors, start=1):
#     print(f"{idx} : {item}")


# names = ["John", "Alex", "Lisa"]
# roll_no = [1,2,3]

# for name, roll_number in zip(names, roll_no):
#     print(f"{name}, roll no. is {roll_number}")



# temp = 40

# while temp < 100:
#     print(f"The current temp is: {temp}")
#     temp += 15
# print(f"The tea is reay to boil.")

# while temp < 100:  
#     temp += 15
#     print(f"The current temp is: {temp}")
# print(f"The tea is reay to boil.")



# orders = ["burger", "coke", "Out of stock", "discontinued"]

# for order in orders:
#     if order == "Out of stock":
#         continue
#     if order == "discontinued":
#         print(f"Discontinued item found. {order}")
#         break
#     print(f"Discontinued item found. {order}")
    
# print("Outside loop")


# names = [("Alex", 17), ("Bam", 12), ("Zara", 13)]

# for name, roll in names:
#     if roll >= 18:
#         print(f"{name} will be seated in class 101.")
#         break
# else:
#         print(f"No one will sit in class 101. ")


# value = 15
# remainder = value % 2

# if remainder:
#     print(f"Not divisible.")

# value = 15
# if (remainder := value % 2):
#     print(f"Not divisible.")



# colors = ["red", "pink", "blue", "green"]

# if (chosen_color := input("Enter your color:")) in colors:
#     print(f"The user chose: {chosen_color}")
# else:
#     print(f"Color not available.")


# numbers = [55,66,77,88]

# print(f"Choose a number: {numbers}")

# while(number := int(input("Choose a number:"))) not in numbers:
#     print(f"Sorry, {number} is not available.")

# print(f"You chose {number}")

users = [{
    "id": 1,
    "total": 100,
    "coupon": "P30"
},
{
    "id": 2,
    "total": 1000,
    "coupon": "P70"
},
{
    "id": 3,
    "total": 200,
    "coupon": "P80"
},
]

discounts = {
    "P30": (0.5, 0),
    "P70": (0.7, 0),
    "P80": (0.8, 0)
}
for user in users:
    percent, fixed = discounts.get(user["coupon"], (0,0))
    discount = user["total"] * percent + fixed
    print(f"{user["id"]} paid {user["total"]} and got discount of {discount}")