snack = input("Insert snack: ").lower()
print(f"User wants {snack}")


if snack == 'cookie' or snack == 'samosa':
    print(f"You chose {snack}")
else:
    print(f"Not available")
