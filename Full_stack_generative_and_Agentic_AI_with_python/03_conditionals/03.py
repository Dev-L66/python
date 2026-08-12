size = input("Enter the cup size you want ").lower()

if size == 'small':
    print(f"For {size}, it is 5 dollars.")
elif size == 'medium':
    print(f"For {size}, it is 15 dollars")
elif size == 'large':
    print(f"For {size}, it is 20 dollars")
else:
    print("Unknown size")
