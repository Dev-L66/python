class InvalidCoffeeError(Exception):
    pass

def bill(flavor, cups):
    menu = {"Latte": 30, "Black coffee": 20}
    try:
        if flavor not in menu:
            raise InvalidCoffeeError("Flavor not available")
        if not isinstance(cups, int):
            raise TypeError("Number of cups must be an int")
        total = menu[flavor] * cups
        print(f"Your bill for {cups} cups of flavor {flavor} is {total}")
    except Exception as e:
        print("Error", e)
    finally:
        print("Thank you for visiting !")

bill("ginger", "two")
bill("mint", 3)
bill("Latte", 2)

    