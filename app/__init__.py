from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

from config import config
from flask_uploads import UploadSet, configure_uploads, IMAGES

bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()
login_manager = LoginManager()
photos = UploadSet('photos', IMAGES)


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    configure_uploads(app, photos)
    # 注册蓝本
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from app.tone import tone as tone_blueprint
    app.register_blueprint(tone_blueprint)

    from app.dict_cmp_accord import dict_cmp_accord as dict_cmp_accord_blueprint
    app.register_blueprint(dict_cmp_accord_blueprint)

    from app.dic_cmp_conduct import dict_cmp_conduct as dic_cmp_conduct_blueprint
    app.register_blueprint(dic_cmp_conduct_blueprint)

    return app
