import asyncio
import aiohttp
from aioresponses import aioresponses

'''позволяет отловить поход в сеть и вернуть заготовленные данные 
with aioresponses() as m:
    m.get(url, payload=dict(crowd=["Andrey", "Alex", "Artem", "Igor"]))
'''

url = "http://service.ru"


async def main():
    with aioresponses() as m:
        m.get(url, payload=dict(crowd=["Andrey", "Alex", "Artem", "Igor"]))
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                json = await response.json()
    print(json)


data = asyncio.run(main())
