import asyncio
import random


async def worker(idx: int, queue: asyncio.Queue):
    while True:
        task_id = await queue.get()
        print(f"worker-{idx} started task-{task_id}")
        await asyncio.sleep(random.randint(1, 3))
        print(f"worker-{idx} finished task-{task_id}")


async def master(queue: asyncio.Queue):
    task_id = 1
    while True:
        await asyncio.sleep(1)
        print(f"master gave task-{task_id}")
        await queue.put(task_id)
        task_id += 1


async def main():
    queue = asyncio.Queue()
    coros = [
        master(queue),
        worker(1, queue),
        worker(2, queue),
        worker(3, queue),
    ]
    await asyncio.gather(*coros)


asyncio.run(main())
