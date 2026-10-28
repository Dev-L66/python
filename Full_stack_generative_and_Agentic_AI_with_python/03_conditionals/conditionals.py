# is_online = True

# if is_online:
#     print(f"User is online")

# snack = input("Enter your preferred snack:").lower()
# print(f"User selected: {snack}")

# if snack == "cookies" or snack == "chips":
#     print(f"Great choice! We' ll serve you with cookies or chips. {snack}")
# else:
#     print(f"Sorry we only serve cookies or chips.")


# color = input(f"Choose a color (red/blue/green)").lower()

# if color == "red":
#     print("Color is red.")
# elif color == "green":
#     print("Color is green.")
# elif color == "blue":
#     print("Color is blue.")
# else:
#     print("Color is not known.")

# status = "active"
# temp = 38

# if status == "active":
#     print(f"Device is active.")
#     if temp > 35:
#         print("High temperature.")
#     else:
#         print("Temperature is normal.")
# else:
#     print("Device is offline.")



# number = int(input("Enter a number:"))

# print(f"User enetered {type(number)}")

# price = 0 if number > 10 else 1
# print(f"The price is {price}")



day = input("Enter the day of week:").lower()

match day:
    case "saturday":
        print("No school.")
    case "sunday":
        print("No school.")
    case "monday":
        print("Working day.")
    case "tuesday":  
          print("Working day.")
    case "wednesday":
        print("Working day.")
    case "thursday":
        print("Working day.")
    case "friday":
        print("No school.")
    case _:
        print("Invalid day.")