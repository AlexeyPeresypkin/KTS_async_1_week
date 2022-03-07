import typing

if typing.TYPE_CHECKING:
    from src.week5.web.app import Application


def setup_routes(app: 'Application'):
    from src.week5.crm.views import AddUserView
    app.router.add_view('/add_user', AddUserView)
