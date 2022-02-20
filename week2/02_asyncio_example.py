import asyncio
import time


async def send_statistic():  # наш "поход" в сторонний сервис
    print(f"{time.time()}: stat")


async def worker():
    while True:
        await asyncio.sleep(60)
        print('end await')
        await send_statistic()


loop = asyncio.get_event_loop()  # получаем loop
loop.create_task(worker())  # добавляем Task в event_loop
loop.run_forever()  # навсегда передаем управлени программы на обработку task-ов добавленных в event loop
