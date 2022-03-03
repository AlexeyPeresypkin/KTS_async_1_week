from aiohttp.web_response import json_response

from src.week5.web.app import View


class AddUserView(View):
    async def post(self):
        self.request.app.database
