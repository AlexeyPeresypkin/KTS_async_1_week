import asyncio
from asyncio import CancelledError


async def db_operation():
    print("operation start")
    try:
        while True:
            print("operation new round")
            await asyncio.sleep(1)
    except CancelledError:
        print("operation was cancelled")
        await asyncio.sleep(1)
    print("operation done")


async def main():
    task = asyncio.create_task(db_operation())
    await asyncio.sleep(5)
    task.cancel()  # вызываем исключение CancelledError внутри db_operation, оно будет обработано как только event loop передаст управление task-е, обрабатывающей эту короутину
    await task  # передаем управление db_operation для корректного завершения


asyncio.run(main())
