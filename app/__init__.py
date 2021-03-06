from flask import Flask
from flask_login import LoginManager

login_manager = LoginManager()

from app.home import home
from app.admin import admin
from app.models import db


# def register_blueprint(app: Flask, blue_print, url_prefix):
#     """
#     注册蓝图
#     """
#     app.register_blueprint(blue_print, url_prefix=url_prefix)


def create_app():
    # static_folder在被传入之后，flask为将路径的basename作为url
    app = Flask(__name__)  # static_url_path='/statics/pics/', static_folder='statics/pics/')
    # app.config.from_object('app.secure_setting')
    # app.config.from_object('app.setting')
    app.config.from_pyfile('secure_setting.py')
    app.config.from_pyfile('setting.py')
    app.debug = app.config['DEBUG']

    app.register_blueprint(home)
    app.register_blueprint(admin, url_prefix='/admin')

    login_manager.init_app(app)
    login_manager.login_view = 'admin.login'

    # mail.init_app(app)

    db.init_app(app)  # 初始化数据库
    db.create_all(app=app)  # 写法一
    # with app.app_context():  # 写法二
    #     db.create_all()

    return app
