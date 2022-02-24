import aiohttp
import asyncio


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://httpbin.org/get') as resp:
            print(resp.status)
            print(await resp.text())


loop = asyncio.get_event_loop()
loop.run_until_complete(main())


# ========================================================


async def req1():
    params = {'key1': 'value1', 'key2': 'value2'}
    async with aiohttp.ClientSession() as session:
        async with session.get('http://httpbin.org/get',
                               params=params) as resp:
            print(await resp.read())
            print(await resp.text())
            print(await resp.json())
            print(resp.status)
            print(resp.headers)


asyncio.run(req1())
