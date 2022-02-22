from dataclasses import dataclass
from task import Task
from yarl import URL
from bs4 import BeautifulSoup
from typing import List
import aiohttp
import asyncio

MAX_DEPTH = 2
PARSED_URLS = set()


@dataclass
class FetchTask(Task):
    url: URL
    depth: int

    def parser(self, data: str) -> List['FetchTask']:
        if self.depth + 1 > MAX_DEPTH:
            return []
        soup = BeautifulSoup(data, 'lxml')
        res = []
        for link in soup.find_all('a', href=True):
            new_url = URL(link['href'])
            if new_url.host is None and new_url.path.startswith('/'):
                new_url = URL.build(
                    scheme=self.url.scheme,
                    host=self.url.host,
                    path=new_url.path,
                    query_string=new_url.query_string
                )
                if new_url in PARSED_URLS:
                    continue
                PARSED_URLS.add(new_url)
                res.append(FetchTask(
                    tid=self.tid,
                    url=new_url,
                    depth=self.depth + 1
                ))
        return res

    async def perform(self, pool):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url) as resp:
                print(self.url, resp.status)
                data = await resp.text()
                res: List[FetchTask] = \
                    await asyncio.get_running_loop().run_in_executor(
                        None, self.parser, data
                    )
                for task in res:
                    await pool.put(task)
