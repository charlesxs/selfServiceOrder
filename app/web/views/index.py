# coding=utf-8
#

from flask import blueprints

bp = blueprints.Blueprint('index', __name__)


@bp.route('/', methods=['GET'])
def index():
    return 'Hello World'


