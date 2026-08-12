seat_type = input("sleeper, ac, general, luxury ").lower()


match seat_type:
    case 'sleeper':
        print("sleeper chosen")
    case "AC":
        print("AC chosen")
    case 'general':
        print("general chosen")
    case "luxury":
        print("luxury chosen")
    case _:
         print("Invalid")
