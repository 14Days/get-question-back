from flask import Flask
from app.controllers.login_out import login_out_page
from app.controllers.secret import secret_page
from app.controllers.registered import registered_page
from app.controllers.questions import questions_page


def register_routers(app: Flask):
    app.register_blueprint(login_out_page)
    app.register_blueprint(secret_page)
    app.register_blueprint(registered_page)
    app.register_blueprint(questions_page)
