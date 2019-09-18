from flask import Flask
from controllers.login_out import login_out_page


def register_routers(app: Flask):
    app.register_blueprint(login_out_page)
