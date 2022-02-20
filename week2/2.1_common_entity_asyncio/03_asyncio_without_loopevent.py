import asyncio
import time


async def send_statistic():
    print(f"{time.time()}: stat")


async def main():
    while True:
        await asyncio.sleep(10)
        await send_statistic()


asyncio.run(main())  # запуск короутины используя упрощенный синтаксис
