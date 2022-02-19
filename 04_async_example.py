import asyncio
import time


async def worker():
    await asyncio.sleep(1)


async def main(count=100):
    begin = time.time()
    await asyncio.gather(
        *[worker() for _ in range(count)]
    )
    print(time.time()-begin)
    
asyncio.run((main()))
