import asyncio
import aiohttp


async def req_post_file():
    async with aiohttp.ClientSession() as session:
        files = {'file': open('../README.md', 'rb')}
        async with session.post('http://httpbin.org/post', data=files) as resp:
            print(await resp.json())


asyncio.run(req_post_file())
