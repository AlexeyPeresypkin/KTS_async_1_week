import asyncio
import random


class Crowd:
    def __init__(self, people: list):
        self._people = people
        self._i = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self._i >= len(self._people):
            raise StopAsyncIteration
        human = self._people[self._i]
        self._i += 1
        delay = random.randint(1, 5)
        await asyncio.sleep(delay)
        return f"wait for {human} {delay}c"


async def main():
    crowd = Crowd(["Andrey", "Alex", "Artem", "Igor"])
    async for i in crowd:
        print(i)


asyncio.run(main())
