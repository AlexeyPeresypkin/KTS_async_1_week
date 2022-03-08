import uuid

from aiohttp.web_exceptions import HTTPNotFound
from aiohttp_apispec import docs, request_schema, response_schema, \
    querystring_schema

from src.week5.crm.models import User
from src.week5.crm.schemes import UserSchema, ListUsersResponseSchema, \
    UserGetRequestSchema, UserGetResponseSchema, UserAddSchema
from src.week5.web.app import View
from src.week5.web.schemes import OkResponseSchema
from src.week5.web.utils import json_response


class AddUserView(View):
    @docs(tags=['crm'], summaey='Add new user',
          description='Add new user in database')
    @request_schema(UserAddSchema)
    @response_schema(OkResponseSchema, 200)
    async def post(self):
        data = self.request['data']
        user = User(email=data['email'], id_=uuid.uuid4())
        await self.request.app.crm_accessor.add_user(user)
        return json_response()


class ListUsersView(View):
    @docs(tags=['crm'], summaey='List users',
          description='List users from database')
    @request_schema(UserSchema)
    @response_schema(ListUsersResponseSchema, 200)
    async def get(self):
        users = await self.request.app.crm_accessor.list_users()
        raw_useres = [{'email': user.email, '_id': str(user.id_)} for user in
                      users]
        return json_response(data={'users': raw_useres})


class GetUsersView(View):
    @docs(tags=['crm'], summaey='Get user',
          description='Get user from database')
    @querystring_schema(UserGetRequestSchema)
    @response_schema(UserGetResponseSchema, 200)
    async def get(self):
        user_id = self.request.query.get('id')
        user = await self.request.app.crm_accessor.get_user(uuid.UUID(user_id))
        if user:
            return json_response(
                data={
                    'user': {'email': user.email, 'id_': str(user.id_)}
                })
        else:
            raise HTTPNotFound
