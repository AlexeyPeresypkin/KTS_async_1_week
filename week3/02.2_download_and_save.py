import asyncio
import aiohttp


async def req_download_file(url: str, destination_path: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            with open(destination_path, 'wb') as fd:
                async for data in resp.content.iter_chunked(1024):
                    fd.write(data)


asyncio.run(req_download_file('url', 'path.png'))
