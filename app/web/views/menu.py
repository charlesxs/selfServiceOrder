# coding=utf-8
#

import os
from flask import Blueprint
from flask import request, Response
from flask import session
from app.db.models.tables import MenuModel
from app.db.models.base import DB
from app.lib.utils import jsonify
from werkzeug.utils import secure_filename

bp = Blueprint('menu', __name__)


@bp.route('/menu', methods=['GET'])
def list_menu():
    query = MenuModel.query.all()
    result = []
    for q in query:
        food = {
            'id': q.mid,
            'name': q.foodname,
            'category': q.category,
            'price': q.price,
            'coupon': q.coupon,
            'imagePath': q.imagepath,
            'intro': q.intro
        }
        result.append(food)
    return jsonify(result)


@bp.route('/edit_menu', methods=['POST'])
def edit_menu():
    data = request.json.get('data')

    # verify and process edit
    for food in data:
        action = food.get('action')
        if action not in ('add', 'delete', 'update'):
            return jsonify(None, status=400, message='操作错误, 只允许添加、删除、和修改')

        if action == 'add':
            q = MenuModel.query\
                .filter(MenuModel.foodname == food['name'])\
                .first()
            if q is not None:
                return jsonify(None, status=400, message='菜单已经存在，不能添加')

            with DB.session.begin(subtransactions=True):
                DB.session.add(MenuModel(
                    foodname=food['name'],
                    category=food.get('category', '川湘菜'),
                    price=food['price'],
                    coupon=food.get('coupon', 0),
                    imagepath=food['imagePath'],
                    intro=food['intro']
                ))
        elif action == 'delete':
            with DB.session.begin(subtransactions=True):
                m = MenuModel.query\
                    .filter(MenuModel.foodname == food['name'])\
                    .first()
                DB.session.delete(m)

        elif action == 'update':
            with DB.session.begin(subtransactions=True):
                DB.session.query(MenuModel)\
                    .filter(MenuModel.mid == food['id'])\
                    .update({
                        'foodname': food['name'],
                        'category': food['category'],
                        'price': food['price'],
                        'coupon': food['coupon'],
                        'imagepath': food['imagePath'],
                        'intro': food['intro']
                    })

    return jsonify(None, status=200, message='成功')


@bp.route('/upload_image', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify(None, status=400, message='没有上传任何文件')

    file = request.files['file']
    filename = secure_filename(file.filename)

    try:
        filepath = os.path.join(os.path.abspath('.'), 'fe/public/assets', filename)

        # ivew upload 插件，此处如果已经存在的文件，再次 save 的话 会触发 自动刷新页面 bug.
        if os.path.isfile(filepath):
            return jsonify({'filename': f'/assets/{filename}'}, status=200, message='文件已经存在')

        # ivew upload 插件，此处如果已经存在的文件，再次 save 的话 会触发 自动刷新页面 bug.
        file.save(filepath)
        return jsonify({'filename': f'/assets/{filename}'}, status=200, message='上传成功')
    except Exception as e:
        return jsonify(None, status=500, message=f'上传失败: {e}')


@bp.route('/delete_image', methods=['POST'])
def delete_image():
    data = request.json.get('data')

    filepath = os.path.join(os.path.abspath('.'), 'fe/public/assets', data['filename'])
    if os.path.isfile(filepath):
        os.remove(filepath)
        return jsonify(None, status=200, message='图片删除成功')
    return jsonify(None, status=404, message='图片不存在')

