import asyncio


async def worker(idx: int):
    while True:
        print(f"worker-{idx} msg")
        await asyncio.sleep(1)


async def main():
    for i in range(3):  # добавляем в event loop 3 task-и
        asyncio.create_task(worker(i + 1))
    while True:
        print(f"main msg")
        await asyncio.sleep(1)
        # сон нужен для передачи управления другим короутинам, нашим worker-ам


asyncio.run(main())
