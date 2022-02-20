import asyncio
import random


async def random_sleep(i: int):
    delay = random.randint(1, 5)
    print(f"{i}: start sleep")
    await asyncio.sleep(delay)
    print(f"{i}: end sleep")


async def main():
    await asyncio.gather(
        random_sleep(1),
        random_sleep(2),
        random_sleep(3),
        random_sleep(4),
        random_sleep(5),
    )


asyncio.run(main())
