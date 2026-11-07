# def brew_chai(flavor):
#     if flavor not in ["masla", "ginger", "elaichi"]:
#         raise ValueError("Flavor not available")
#     print(f"brewing {flavor} chai")

# # brew_chai("apple")
# brew_chai("ginger")



class OutOFIngredientsError(Exception):
    pass

def make_coffee(milk, sugar):
    if milk == 0 or sugar == 0:
        raise OutOFIngredientsError("Missing milk or sugar")
    print("coffee is ready")

make_coffee(0, 1)