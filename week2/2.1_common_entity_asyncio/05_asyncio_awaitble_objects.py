import asyncio


async def coro():
    await asyncio.sleep(5)


async def main():
    await coro()  # дожидаемся выполнения короутины
    task = asyncio.create_task(coro())
    # создаем Task и добавляем ее в event loop
    await task  # дожидаемся выполнения Task-и


asyncio.run(main())
