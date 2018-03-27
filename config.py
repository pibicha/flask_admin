# 配置基类
class Config:
    GENERATE_DATABASE_URL = 'flask-sqlacodegen --outfile ./app/models.py  --flask mysql+pymysql://user:password@ipaddress/dbname'
    SECRET_KEY = 'nishengri'
    UPLOADED_PHOTOS_DEST = r'd:\files\dict_imgs'

    # sqlAlchemy相关配置
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # SQLALCHEMY_ECHO = True
    PER_PAGE = 20

    # 由子类实现，类似java的模板方法，可以对app进行扩展
    @staticmethod
    def init_app(app):
        pass


class Dev(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://name:password@ip/dbname'


class ProductionConfig(Config):
    @classmethod
    def init_app(cls, app):
        from werkzeug.contrib.fixers import ProxyFix
        app.wsgi_app = ProxyFix(app.wsgi_app)

    SQLALCHEMY_DATABASE_URI = 'mysql://name:password@ip/dbname'


config = {
    'development': Dev,
    'production': ProductionConfig,
    'default': Dev
}
