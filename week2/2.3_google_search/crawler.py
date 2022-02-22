import asyncio
from dataclasses import dataclass
from typing import Optional
from task import Task
from fetch_task import FetchTask
from yarl import URL


class Pool:
    def __init__(self, max_rate: int, interval: int = 1,
                 concurrent_level: Optional[int] = None):
        self.max_rate = max_rate
        self.interval = interval
        self.concurrent_level = concurrent_level
        self.is_running = False
        self._queue = asyncio.Queue()
        self._scheduler_task: Optional[asyncio.Task] = None
        self._sem = asyncio.Semaphore(concurrent_level or max_rate)
        self._concurrent_workers = 0
        self._stop_event = asyncio.Event()

    async def _worker(self, task: FetchTask):
        async with self._sem:
            self._concurrent_workers += 1
            await task.perform(self)
            self._queue.task_done()
        self._concurrent_workers -= 1
        if not self.is_running and self._concurrent_workers == 0:
            self._stop_event.set()

    async def _scheduler(self):
        while self.is_running:
            for _ in range(self.max_rate):
                async with self._sem:
                    task = await self._queue.get()
                    asyncio.create_task(self._worker(task))
            await asyncio.sleep(self.interval)

    async def start(self):
        self.is_running = True
        self._scheduler_task = asyncio.create_task(self._scheduler())

    async def put(self, task: FetchTask):
        await self._queue.put(task)

    async def join(self):
        await self._queue.join()

    async def stop(self):
        self.is_running = False
        if self._concurrent_workers != 0:
            await self._stop_event.wait()
        self._scheduler_task.cancel()


async def start(pool):
    await pool.put(
        FetchTask(
            tid=1,
            url=URL('https://habr.com/ru/company/kts/blog/'),
            depth=1
        )
    )
    await pool.start()
    await pool.join()
    await pool.stop()


def main():
    loop = asyncio.get_event_loop()
    pool = Pool(3)
    try:
        loop.run_until_complete(start(pool))
    except KeyboardInterrupt:
        loop.run_until_complete(pool.stop())
        loop.close()


if __name__ == '__main__':
    main()
