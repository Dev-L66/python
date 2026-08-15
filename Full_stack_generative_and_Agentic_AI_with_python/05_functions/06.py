# scopes

# local scope - inside a func
# enclosing from outer func if nested

# global- top level script

#  built in


def greeting():
    greet = "hello" # local scope
    print(f"Inside func {greet}")

greet = "Hi"
greeting()
print(f"From outside func {greet}")


def greet_count():
    greet = "Hello world"
    def print_order():
        greet = "HIHI"
        print("inner", greet)
    print_order()
    print("Outer, greet")

greet = "global greeting" # global
greet_count()
print("Global,",greet)