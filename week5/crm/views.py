import uuid

from aiohttp.web_response import json_response

from src.week5.crm.models import User
from src.week5.web.app import View


class AddUserView(View):
    async def post(self):
        data = await self.request.json()
        user = User(email=data['email'], _id=uuid.uuid4())
        await self.request.app.crm_accessor.add_use(user)
        return json_response(data={'status': 'ok'})
