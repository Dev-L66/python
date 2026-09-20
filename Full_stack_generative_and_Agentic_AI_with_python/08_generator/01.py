# generators 
# memory is saved
# sometimes you don't want the result immediately
# lazy evaluation


def serve_drink():
    yield "Cup1: Coffee"
    yield "Cup2: Juice"


stall = serve_drink()

for cup in stall:
    print(cup)


def get_drink_list():
    return ["Cup1", "Cup2", "Cup3"]


def get_drink():
    yield "Cup1: Coffee"
    yield "Cup2: Juice"


drinks = get_drink()
print(drinks)

print(next(drinks))
print(next(drinks))
# print(next(drinks))