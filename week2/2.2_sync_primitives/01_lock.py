import asyncio


class PackOfChips:
    def __init__(self):
        self._lock = asyncio.Lock()

    async def reserve(self):
        await self._lock.acquire()

    def cheeps(self):
        self._lock.release()


async def handle(name: str, pack: PackOfChips):
    await pack.reserve()  # первая короутина, которая дошла до этого места заблокирует доступ и продолжит выполнение, а остальные - ждать освобождения ресурсов
    print(f"{name} put hand in pack")
    await asyncio.sleep(1)  # сон показывает, что все остальные короутины
    # заблокированы на await pack.reserve()
    pack.cheeps()  # освобождаем ресурсы
    print(f"{name} took cheeps")


async def main():
    people = ["Andrey", "Alex", "Artem", "Igor"]
    pack = PackOfChips()
    await asyncio.gather(*[handle(name, pack) for name in people])
    # запускаем параллельно нескольно короутин


asyncio.run(main())
