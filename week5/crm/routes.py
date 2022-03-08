import typing

if typing.TYPE_CHECKING:
    from src.week5.web.app import Application


def setup_routes(app: 'Application'):
    from src.week5.crm.views import AddUserView, ListUsersView, GetUsersView
    app.router.add_view('/add_user', AddUserView)
    app.router.add_view('/list_users', ListUsersView)
    app.router.add_view('/get_user', GetUsersView)
