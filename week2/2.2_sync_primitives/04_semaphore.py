import asyncio
import time


class Query:
    async def execute(self):
        await asyncio.sleep(1)


class PGStore:
    def __init__(self):
        self._sem = asyncio.Semaphore(2)
        # ограничиваем число одновременных доступов к ресурсам до 2
        self._init_time = time.time()

    async def execute_request(self, query):
        async with self._sem:  # каждое использование контекстного менеджера будет уменьшать счетчик семафора и когда счетчик станет равным 0 - короутины, ранее не выполнившие async with self._sem - заблокируются
            print(f"{time.time() - self._init_time} request was started")
            await query.execute()
            print(f"{time.time() - self._init_time} request was handled")


async def main():
    store = PGStore()
    coros = [store.execute_request(Query()) for _ in range(100)]
    await asyncio.gather(*coros)


asyncio.run(main())
