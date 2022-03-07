import typing
from typing import Optional

from src.week5.crm.models import User

if typing.TYPE_CHECKING:
    from src.week5.web.app import Application


class CrmAccessor:
    def __init__(self):
        self.app: Optional[Application] = None

    async def connect(self, app: "Application"):
        self.app = app
        try:
            self.app.database['users']
        except KeyError:
            self.app.database['users'] = []
            print('connect database')

    async def disconnect(self, app: "Application"):
        self.app = None
        print('disconnect from database')

    async def add_use(self, user: User):
        self.app.database['users'].append(user)
