import asyncio
from asyncio import CancelledError


async def worker(idx: int):
    try:
        while True:
            print(f"worker {idx} new iter")
            await asyncio.sleep(1)
    except CancelledError:
        print(f"worker was cancelled")
    print(f"worker was correctly cancelled")


async def worker_with_exception(idx: int):
    await asyncio.sleep(1)
    print(f"worker {idx} Exception")
    raise Exception


async def main():
    done, pending = await asyncio.wait(
        [*[worker(i) for i in range(1, 4)], worker_with_exception(4)],
        return_when=asyncio.FIRST_EXCEPTION,
    )
    # Внутри pending будут перечислены все работающие таски, которые ещё обрабатываются в данный момент
    print(f"done({len(done)}) pending({len(pending)})")
    # показываем число завершенный и работающих task-ов
    for p in pending:
        p.cancel()
    await asyncio.gather(*pending)


asyncio.run(main())
