import threading
import time


def monitor_tea_temp():
  while True:
    print(f"Monitoring temp")
    time.sleep(2)


t = threading.Thread(target=monitor_tea_temp, daemon=
                     True)
t.start()

print("MAin program done")