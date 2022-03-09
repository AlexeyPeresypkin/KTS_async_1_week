from typing import Optional

from aiohttp.web import Application as AiohttpApplication, \
    run_app as aiohttp_run_app, View as AiohttpView, Request as AiohttpRequest
from aiohttp_apispec import setup_aiohttp_apispec

from src.week5.store import setup_accessor
from src.week5.store.crm.accessor import CrmAccessor
from src.week5.web.config import Config, setup_config
from src.week5.web.middlewares import setup_middlewares
from src.week5.web.routes import setup_routes


class Application(AiohttpApplication):
    config: Optional[Config] = None
    database: dict = {}
    crm_accessor: Optional[CrmAccessor] = None


class Request(AiohttpRequest):
    @property
    def app(self) -> Application:
        return super().app


class View(AiohttpView):
    @property
    def request(self) -> Request:
        return super().request


app = Application()


def run_app():
    setup_config(app)
    setup_routes(app)
    setup_aiohttp_apispec(app,
                          title='CRM Application',
                          url='/docs/json',
                          swagger_path='/docs'
                          )
    setup_middlewares(app)
    setup_accessor(app)
    aiohttp_run_app(app)
