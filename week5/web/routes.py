from aiohttp.web_app import Application
from src.week5.crm.routes import setup_routes as crm_setup_routes


def setup_routes(app: Application):
    crm_setup_routes(app)
