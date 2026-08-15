def greeting():
    # return "Hello"
    print("Hello")


# print(greeting())
return_val = greeting()
print(return_val)



def function1():
    pass

print(function1())


def hello():
    return "HI"

gr = hello()
print(gr)


def status(chairs_left):
    if chairs_left == 0:
        return "Sorry no chair left"
    return "Food is ready"
    print("anthing after return statement won't be printed")

print(status(0))
print(status(5))




def report():
    return 100, 200, 300

sold, remaining, _ = report()

print(f"Sold: {sold} Remaining: {remaining}")