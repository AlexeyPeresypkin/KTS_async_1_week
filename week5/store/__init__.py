import typing

from src.week5.store.crm.accessor import CrmAccessor

if typing.TYPE_CHECKING:
    from src.week5.web.app import Application


def setup_accessor(app: "Application"):
    app.crm_accessor = CrmAccessor()
    app.on_startup.append(app.crm_accessor.connect)
    app.on_cleanup.append(app.crm_accessor.disconnect)


