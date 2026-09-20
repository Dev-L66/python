# infinite generators


# streaming or realtime systems, drain memory


def infinite_drink():
    count=1
    while True:
        yield f"""Refil {count}"""

        count += 1

refill = infinite_drink()

user2 = infinite_drink()

for _ in range(3):
    print(next(refill))

for _ in range(6):
    print(user2(refill))