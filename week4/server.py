from aiohttp import web
from get_data import get_data

app = web.Application()


class View(web.View):
    async def get(self):
        data = get_data(self.request)
        print(data)
        return web.json_response(data)
        # print(self.request.method)
        # print(web.Response.body)
        # return web.Response(status=200, text='Hi')

    async def post(self):
        print(self.request)

    async def delete(self):
        pass

    async def put(self):
        pass

    async def patch(self):
        pass

    async def options(self):
        pass

    async def head(self):
        pass


app.add_routes([web.route('*', '/{tail:.*}', View)])

if __name__ == '__main__':
    web.run_app(app, port=9090, print=lambda _: _)
