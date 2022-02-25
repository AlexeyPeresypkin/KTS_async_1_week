import asyncio
import aiohttp


async def req_multipart_post():
    async with aiohttp.ClientSession() as session:
        data = aiohttp.FormData()
        data.add_field('file1',
                       open('README.md', 'rb'),
                       filename='README.md',
                       content_type='text/plain')
        data.add_field('file2',
                       open('README.md', 'rb'),
                       filename='README.md',
                       content_type='text/plain')
        async with session.post('http://httpbin.org/post', data=data) as resp:
            print(await resp.json())


asyncio.run(req_multipart_post())
