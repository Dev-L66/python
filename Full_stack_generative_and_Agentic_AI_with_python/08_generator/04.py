def local_drink():
    yield "Coffee"
    yield "Cold Coffee"

def imported_drinks():
    yield "Match"
    yield "Oolong"


def menu():
    yield from local_drink()
    yield from imported_drinks()


for drink in menu():
   print(drink)


def stall():
    try:
        while True:
            order = yield "Waiting for order"
    except:
        print("Stall closed")

stall_drink = stall()

print(next(stall_drink))
stall_drink.close()