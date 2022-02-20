import asyncio
import random
from asyncio import ALL_COMPLETED


async def random_sleep(i: int):
    delay = random.randint(1, 5)
    print(f"{i}: start sleep")
    await asyncio.sleep(delay)
    print(f"{i}: end sleep")


async def main():
    await asyncio.wait([random_sleep(i) for i in range(1, 6)],
                       return_when=ALL_COMPLETED)


asyncio.run(main())
