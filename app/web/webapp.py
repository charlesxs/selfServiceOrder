# coding=utf-8
#

from datetime import timedelta
from flask import Flask
from app.db.models.base import DB
from app.config import CONF

from app.web.views.index import bp as index_bp


def make_app():
    app = Flask('web')
    app.secret_key = 'self_service_order_secret'
    app.permanent_session_lifetime = timedelta(days=1)
    app.config['SQLALCHEMY_DATABASE_URI'] = CONF.db.connection
    app.config['SQLALCHEMY_POOL_SIZE'] = CONF.db.pool_size
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # register blueprint
    app.register_blueprint(index_bp, url_prefix='')

    # init plugins
    DB.init_app(app)
    return app


def run():
    app = make_app()
    app.run()

