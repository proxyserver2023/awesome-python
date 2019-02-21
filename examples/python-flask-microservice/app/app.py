import connexion
from connexion import RestyResolver
from flask_injector import FlaskInjector
from injector import Binder


def configure(binder: Binder) -> Binder:
    binder.bind(
    )
    return binder


if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='swagger/')
    app.add_api('api.yaml', resolver=RestyResolver('api'))
    FlaskInjector(app=app.app, modules=[configure])
    app.run(port=8080)
