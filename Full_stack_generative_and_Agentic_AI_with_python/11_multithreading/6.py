import threading
import time


def prepare_coffee(type_, wait_time):
    print(f"{type_} coffee brewing")
    time.sleep(2)
    print(f"{type_} coffee ready")


t1 = threading.Thread(target=prepare_coffee, args=("LAtte", 2))

t2 = threading.Thread(target=prepare_coffee, args=("Black", 3))


start = time.time()

t1.start()
t2.start()
t1.join()
t2.join()

end = time.time()

print(f"Time taken {end-start}")