#  types of functions

# pure vs impure
#  recursve functions
# lambda functions or anonymous functions


def pure_func(greet):
    return greet * 10

# print(pure_func("hello"))




# not recommended
greeting = "HIHIH"
def impure_func(greet):
    global greeting
    greeting += greet


# recursive - function calling itself


def pour(n):
    print("Pouring....", n)
    if n == 0:  
        return "All poured"
    return pour(n - 1)

abc = pour(5)
print(abc)


# lambda

names = ["Ali", "Alex", "Hana", "Alan"]

strong_name = list(filter(lambda name: name == "Hana", names))
# strong_name = list(filter(lambda name: name != "Hana", names))
print(strong_name)


