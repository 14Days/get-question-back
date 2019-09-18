from flask import Flask
from controllers.login_out import login_out_page
from controllers.secret import secret_page


def register_routers(app: Flask):
    app.register_blueprint(login_out_page)
    app.register_blueprint(secret_page)
