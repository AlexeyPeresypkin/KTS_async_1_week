from aiohttp import web
from get_data import get_data

app = web.Application()


class View(web.View):
    async def get(self):
        data = get_data(self.request)
        return web.json_response(data)

    async def post(self):
        data = get_data(self.request)
        return web.json_response(data)

    async def delete(self):
        data = get_data(self.request)
        return web.json_response(data)

    async def put(self):
        data = get_data(self.request)
        return web.json_response(data)

    async def patch(self):
        data = get_data(self.request)
        return web.json_response(data)

    async def options(self):
        data = get_data(self.request)
        return web.json_response(data)

    async def head(self):
        data = get_data(self.request)
        return web.json_response(data)


app.add_routes([web.route('*', '/{tail:.*}', View)])

if __name__ == '__main__':
    web.run_app(app, port=9090, print=lambda _: _)
