from flask import Flask
from app.config import FlaskConfig
from app.controllers import register_routers
from app.models import connect_db


def new_flask_app() -> Flask:
    app = Flask(__name__)

    # 添加配置文件
    app.config.from_object(FlaskConfig)

    # 注册路由
    register_routers(app)

    # 链接数据库
    connect_db(app)

    return app
