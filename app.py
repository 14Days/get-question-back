from flask import Flask
from controllers import register_routers


def new_flask_app():
    app = Flask(__name__)

    register_routers(app)

    return app
