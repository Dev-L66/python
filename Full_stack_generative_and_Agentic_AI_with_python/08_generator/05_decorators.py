# decorators

# wrapper around function

from functools import wraps

def my_decorator(func):
    # @wraps preserves func name
    @wraps(func) 
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper

@my_decorator
def greet():
    print("Hello from decorator.")

greet()
print(greet.__name__)