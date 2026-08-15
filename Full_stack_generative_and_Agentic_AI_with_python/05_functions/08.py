greet = "Hello"


def greeting():
    # greet = "HI"
    def world():
        # nonlocal greet
        global greet
        greet = "HIHIHI"
    world()

greeting()
print(f"Final global {greet}")