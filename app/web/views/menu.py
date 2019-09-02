# coding=utf-8
#

from flask import Blueprint
from flask import request, Response
from flask import session
from app.db.models.tables import MenuModel
from app.db.models.base import DB

bp = Blueprint('menu', __name__)


@bp.route('/menu', methods=['GET'])
def list_menu():
    if not session.get('is_login'):
        return Response({
            'code': 403,
            'message': 'require login'
        }, status=403, content_type='application/json')
    query = MenuModel.query.all()
    result = []
    for q in query:
        food = {
            'id': q.mid,
            'name': q.foodName,
            'category': q.category,
            'price': q.price,
            'coupon': q.coupon,
            'imgPath': q.imgPath,
            'intro': q.intro
        }
        result.append(food)

    return Response({
        'code': 200,
        'message': 'success',
        'data': result
    }, status=200, content_type='application/json')


@bp.route('/edit_menu', methods=['POST'])
def edit_menu():
    if not session.get('is_login'):
        return Response({
            'code': 403,
            'message': 'require login'
        }, status=403, content_type='application/json')

    data = request.json.get('data')

    # verify and process edit
    for food in data:
        action = food.get('action')
        if action not in ('add', 'delete', 'update'):
            raise Exception(u'操作错误, 只允许添加、删除、和修改')

        if action == 'add':
            q = MenuModel.query\
                .filter(MenuModel.foodname == food['name'])\
                .first()
            if q is not None:
                raise Exception(u'菜单已经存在，不能添加')

            DB.session.add(MenuModel(
                foodname=food['name'],
                category=food['category'],
                price=food['price'],
                coupon=food['coupon'],
                imgPath=food['imgPath'],
                intro=food['intro']
            ))
            DB.session.commit()

        elif action == 'delete':
            m = MenuModel.query\
                .filter(MenuModel.mid == food['id'])\
                .first()
            DB.session.delete(m)

        elif action == 'update':
            DB.session.begin(subtransactions=True)
            DB.session.query(MenuModel)\
                .filter(MenuModel.mid == food['id'])\
                .update({
                    'name': food['name'],
                    'category': food['category'],
                    'price': food['price'],
                    'coupon': food['coupon'],
                    'imgPath': food['imgPath'],
                    'intro': food['intro']
                })
            DB.session.commit()

    return Response({
        'code': 200,
        'message': 'success'
    }, status=200, content_type='application/json')



