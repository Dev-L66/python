from multiprocessing import Process
import time


def brew_coffee(name):
    print(F"Start of {name} coffee brewing")
    time.sleep(3)
    print(f"End of {name} coffee brewing")


if __name__ == "__main__":
  coffee_makers = [
    Process(target = brew_coffee, args=(f"Coffee maker {i+1}", ))
    for i in range(3)
]

#    start all processes
  for p in coffee_makers:
    p.start()
#  wait for all to complete
  for p in coffee_makers:
    p.join()

print("All coffe served")