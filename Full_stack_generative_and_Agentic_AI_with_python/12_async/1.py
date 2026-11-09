import asyncio
import time

# async def brew_coffee():
#     print("BRewing")
#     await asyncio.sleep(2)
#     print("Coffee is ready")

# asyncio.run(brew_coffee())



async def brew(name):
    print(f"Brewing {name}")
    # time.sleep(2)
    await asyncio.sleep(2)
    print(f"Ready {name}")

async def main():
    await asyncio.gather(
    brew("Latte"),
    brew("Black"))

asyncio.run(main())

