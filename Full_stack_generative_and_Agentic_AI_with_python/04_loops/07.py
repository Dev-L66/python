# walrus operator :=

# val = 10
# remainder = val % 3

# if remainder:
#     print(f"not divisible, reminder {remainder}")


val = 10

# if remainder = val % 3: not allowed
#     print(f"not divisible, remainder is {remainder}")
if remainder := val % 3:
    print(f"not divisible, remainder is {remainder}")



colors = ["red", "blue", "green"]

if (color := input("Enter your color ")) in colors:
    print(f"Color chosen: {color}")
else:
    print(f"Color not available")



flavors = ["vanilla", "chocolate", "cotton candy", "cookies and cream"]

print(f"Available flavors", flavors)

while(flavor := input("Choose your flavor ")) not in flavors:
    print(f"Sorry {flavor} not available")
print(f"You chose {flavor}")