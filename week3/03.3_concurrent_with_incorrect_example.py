import asyncio
import os
import asyncpg


async def get_connection_by_dsn():
    """
    POSTGRES_DSN = postgres://user:password@host:port/database
    """
    return await asyncpg.connect(os.getenv("POSTGRES_DSN"))


async def query(conn):
    print(await conn.fetch("select * from users"))


async def incorrect():
    conn = await get_connection_by_dsn()
    await asyncio.gather(query(conn), query(conn))


asyncio.run(incorrect())
