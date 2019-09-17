from flask import Flask
from controllers.hello import hello_blueprint


def register_routers(app: Flask):
    app.register_blueprint(hello_blueprint, url_prefix='/hello')
