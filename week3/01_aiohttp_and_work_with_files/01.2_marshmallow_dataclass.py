from dataclasses import field
from typing import Optional, ClassVar, Type

import aiohttp
import marshmallow_dataclass
from marshmallow import Schema, EXCLUDE

data = {'args': {},
        'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate',
                    'Host': 'httpbin.org',
                    'User-Agent': 'Python/3.9 aiohttp/3.7.4',
                    'X-Amzn-Trace-Id': 'Root=1-617aba18-145c6e6e52f9114866736666'},
        'origin': '95.84.229.15', 'url': 'http://httpbin.org/get'}


@marshmallow_dataclass.dataclass
class Headers:
    accept: str = field(metadata={'data_key': 'Accept'})
    accept_encoding: str = field(metadata={'data_key': 'Accept-Encoding'})
    host: str = field(metadata={'data_key': 'Host'})
    user_agent: str = field(metadata={'data_key': 'User-Agent'})
    x_amzn_trace_id: Optional[str] = field(default=None, metadata={
        'data_key': 'X-Amzn-Trace-Id'})

    class Meta:
        unknown = EXCLUDE


@marshmallow_dataclass.dataclass
class GetResponse:
    args: dict
    headers: Headers
    origin: str
    url: str


class Meta:
    unknown = EXCLUDE


GetResponseSchema = marshmallow_dataclass.class_schema(GetResponse)
GetResponseSchema().load(data)


# <=>
@marshmallow_dataclass.dataclass
class GetResponse:
    args: dict
    headers: Headers
    origin: str
    url: str

    Schema: ClassVar[Type[Schema]] = Schema

    class Meta:
        unknown = EXCLUDE


GetResponse.Schema().load(data)


async def req() -> GetResponse:
    async with aiohttp.ClientSession() as session:
        async with session.get('http://httpbin.org/get') as resp:
            data = await resp.json()
            res = GetResponse.Schema().load(data)
            print(res)
            return res
