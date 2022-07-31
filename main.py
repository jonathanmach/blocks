from flask import Flask

from blueprints import register_blueprints
# from flask_injector import FlaskInjector

# from core.dependencies import configure


def create_app():
    app = Flask(__name__)
    register_blueprints(app)


    @app.route("/")
    def hello_world():
        return "Hello, World!"

    # Setup Flask Injector, this has to happen AFTER routes are added
    # FlaskInjector(app=app, modules=[configure])

    return app


