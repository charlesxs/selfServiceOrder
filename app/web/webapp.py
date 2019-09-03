# coding=utf-8
#

from datetime import timedelta
from flask import Flask
from app.db.models.base import DB
from app.config import CONF


def make_app():
    app = Flask('web')
    app.secret_key = 'self_service_order_secret'
    app.permanent_session_lifetime = timedelta(days=1)
    app.config['SQLALCHEMY_DATABASE_URI'] = CONF.db.connection
    app.config['SQLALCHEMY_POOL_SIZE'] = CONF.db.pool_size
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # register blueprint
    from app.web.views.index import bp as index_bp
    app.register_blueprint(index_bp, url_prefix='')

    from app.web.views.menu import bp as menu_bp
    app.register_blueprint(menu_bp, url_prefix='')

    from app.web.views.order import bp as order_bp
    app.register_blueprint(order_bp, url_prefix='')

    from app.web.views.statistics import bp as s_bp
    app.register_blueprint(s_bp, url_prefx='')

    from app.web.views.employee import bp as e_bp
    app.register_blueprint(e_bp, url_prefix='')

    # init plugins
    DB.init_app(app)
    return app


def run():
    app = make_app()
    app.run()

