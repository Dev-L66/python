def update_order():
    greet = "hello"

    def greeting():
        # nonlocal greet
        greet = "hello world"
    greeting()
    print(f"After greeting update {greet}")

update_order()