# file = open("order.txt", "w")
# try:
#    file.write("Hello world!!!!!!!")
# finally:
#    file.close()


with open("order.txt", "w") as file:
    file.write("Hello world 2!!!!!!!!")