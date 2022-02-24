from dataclasses import dataclass
from typing import Optional

import aiohttp

d = {'args': {},
     'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate',
                 'Host': 'httpbin.org',
                 'User-Agent': 'Python/3.9 aiohttp/3.7.4',
                 'X-Amzn-Trace-Id': 'Root=1-617aba18-145c6e6e52f9114866736666'},
     'origin': '95.84.229.15', 'url': 'http://httpbin.org/get'}


# описанный ответ с помощью dataclass
@dataclass
class Headers:
    accept: str
    accept_encoding: str
    host: str
    user_agent: str
    x_amzn_trace_id: Optional[str] = None


@dataclass
class GetResponse:
    args: dict
    headers: Headers
    origin: str
    url: str


async def req() -> GetResponse:
    async with aiohttp.ClientSession() as session:
        async with session.get('http://httpbin.org/get') as resp:
            data = await resp.json()
            headers_dict = data.get('headers', {})
            headers = Headers(
                accept=headers_dict['Accept'],
                accept_encoding=headers_dict['Accept-Encoding'],
                host=headers_dict['Host'],
                user_agent=headers_dict['User-Agent'],
                x_amzn_trace_id=headers_dict['X-Amzn-Trace-Id']
            )
            res = GetResponse(
                args=data['args'],
                headers=headers,
                origin=data['origin'],
                url=data['url']
            )
            return res
