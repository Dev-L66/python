# send value to generators

def customers():
    print("Welcome! What drink would you like?")
    order = yield
    while True:
        print(f"""PReparing {order}""")
        order = yield

stall = customers()

next(stall)

stall.send("Coffee")
stall.send("Cold Coffee")