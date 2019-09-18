from flask import Flask
from config import FlaskConfig
from controllers import register_routers
from models import connect_db


def new_flask_app() -> Flask:
    app = Flask(__name__)

    # 添加配置文件
    app.config.from_object(FlaskConfig)

    # 注册路由
    register_routers(app)

    # 链接数据库
    connect_db(app)

    return app
