from .party import party

services = [{"service": party, "prefix": "/party"}]


def registerService(app):
    for service in services:
        app.register_blueprint(
            blueprint=service.get("service"), url_prefix=service.get("prefix")
        )
