from flask import Flask
from controllers.login_out import login_out_page
from controllers.secret import secret_page
from controllers.registered import registered_page


def register_routers(app: Flask):
    app.register_blueprint(login_out_page)
    app.register_blueprint(secret_page)
    app.register_blueprint(registered_page)
