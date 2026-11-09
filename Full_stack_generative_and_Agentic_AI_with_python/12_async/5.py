import asyncio
import threading

import time


def background_worker():
    while True:
        time.sleep(2)
        print(f"Logging the system")

async def fetch_order():
    await asyncio.sleep(3)
    print("Order fetched")


threads = threading.Thread(target = background_worker, daemon=True)
threads.start()


asyncio.run(fetch_order())