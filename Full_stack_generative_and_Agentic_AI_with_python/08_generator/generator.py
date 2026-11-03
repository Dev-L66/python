# def hello():
#     yield "Hi, how are you?"
#     yield "Hiiiiiiiiii!"
#     yield "Hello world!"


# greetings = hello()

# for greeting in greetings:
#     print(greeting)



#     def get_list():
#         return ["red", "blue", "green"]

#     def get_list_get():
#         yield "red"
#         yield "blue"
#         yield "green"

# colors = get_list_get()
# print(colors)
# print(next(colors))
# print(next(colors))
# print(next(colors))
# print(next(colors))


# def infinite_coffee():
#     count = 1
#     while True:
#         yield f"Refill {count}"
#         count += 1

# refill = infinite_coffee()
# user2 = infinite_coffee()

# for _ in range(5):
#     print(next(refill))

# for _ in range(6):
#     print(next(user2))


# def customer():
#     print("Welcome! What would you like?")
#     order = yield
#     while True:
#         print(f"Preparing {order}")
#         order = yield

# stall = customer()
# next(stall)

# stall.send("Pizza")


# def local_coffee():
#     yield "Cold coffee"
#     yield "Latte"

# def imported_coffee():
#     yield "coffee 1"
#     yield "Coffee 2"

# def menu():
#     yield from local_coffee()
#     yield from imported_coffee()

# for coffee in menu():
#     print(coffee)



# def coffee_stall():
#     try:
#         while True:
#             order = yield "Waiting for order"
#     except:
#         print("Stall closed")


# stall = coffee_stall()
# print(next(stall))
# stall.close() # cleanup of memory

# from functools import wraps

# def my_decorator(func):
#     @wraps(func)
#     def wrapper():
#         print("Before fnction runs.")
#         func()
#         print("After function runs.")
#     return wrapper

# @my_decorator
# def greet():
#     print("Hello from decorator.")

# greet()
# print(greet.__name__)






# from functools import wraps

# def log_activity(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f"Calling: {func.__name__}")
#         result = func(*args, **kwargs)
#         print(f"Finished: {func.__name__}")
#         return result
#     return wrapper


# @log_activity
# def brew_coffee(type, milk="no"):
#     print(f"Brewing {type} and milk status: {milk} ")

# brew_coffee("Cold coffee")




from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("Access denied")
            return None
        else:
            return func(user_role)

    return wrapper


@require_admin
def access_inventory(role):
    print(f"Access granted: {role}")

access_inventory("user")
access_inventory("admin")