# coding=utf-8
#

import hashlib
from flask import Blueprint
from flask import request, session
from app.db.models.tables import UserModel
from app.lib.utils import jsonify

bp = Blueprint('index', __name__)


@bp.route('/', methods=['GET'])
def index():
    return 'Hello World'


@bp.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify(None, status=200, message='缺少用户名或密码')

    um = UserModel.query.\
        filter(UserModel.username == username)\
        .first()
    if not um:
        return jsonify(None, status=200, message='用户名不存在')

    enpass = hashlib.md5(password.encode()).hexdigest()
    if enpass != um.password:
        return jsonify(None, status=200, message='密码错误')

    session['username'] = username
    return jsonify(None, status=200)


@bp.route('/logout', methods=['GET'])
def logout():
    username = session.get('username')
    if not username:
        return jsonify(None, status=200, message='用户没有登录')

    session.clear()
    return jsonify(None)

