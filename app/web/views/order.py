# coding=utf-8
#

import uuid
from datetime import datetime
from flask import Blueprint
from flask import request, Response
from flask import session
from app.db.models.tables import OrderModel, OrderDetailModel, MenuModel
from app.db.models.base import DB

bp = Blueprint('order', __name__)


@bp.route('/generate_order', methods=['POST'])
def generate_order():
    if not session.get('is_login'):
        return Response({
            'code': 403,
            'message': 'require login'
        }, status=403, content_type='application/json')

    data = request.json.get('data')

    # 生成订单ID
    order_id = uuid.uuid4()

    # 生成订单
    order = OrderModel(
        oid=order_id,
        status=u'已下单',
        create_time=datetime.now(),
        update_time=datetime.now(),
        amount=data['amount'],
        payment_status=u'未支付'
    )
    # 写入DB
    DB.session.begin(transactions=True)
    DB.session.add(order)
    DB.session.commit()

    # 写订单详情表
    for food in data['detail']:
        DB.session.begin(transactions=True)
        DB.session.add(OrderDetailModel(
            oid=order_id,
            mid=food['id']
        ))
        DB.session.commit()
    return Response({
        'code': 200,
        'message': 'success'
    }, status=200, content_type='application/json')


@bp.route('/order', methods=['GET'])
def order():
    if not session.get('is_login'):
        return Response({
            'code': 403,
            'message': 'require login'
        }, status=403, content_type='application/json')

    uid = session.get('uid')
    orders = OrderModel.query\
        .filter(OrderModel.uid == uid)\
        .all()

    result = []
    for o in orders:
        o_map = {
            'oid': o.oid,
            'status': o.status,
            'create_time': o.create_time,
            'update_time': o.update_time,
            'comment': o.comment,
            'amount': o.amount,
            'payment_status': o.payment_status
        }

        details_models = DB.session.query(OrderDetailModel)\
            .join(MenuModel, OrderDetailModel.mid == MenuModel.id)\
            .filter(OrderDetailModel.oid == o.oid).all()

        o_map['detail'] = [{'id': d.id, 'name': d.name, 'price': d.price} for d in details_models]
        result.append(o_map)

    return Response({
        'code': 200,
        'message': 'success',
        'data': result
    }, status=200, content_type='application/json')


@bp.route('/edit_order', methods=['POST'])
def edit_order():
    if not session.get('is_login'):
        return Response({
            'code': 403,
            'message': 'require login'
        }, status=403, content_type='application/json')

    data = request.json.get('data')
    for order in data:
        DB.session.begin(transactions=True)
        DB.session.query(OrderModel)\
            .filter(OrderModel.oid == order['oid'])\
            .update({
                'amount': order['amount'],
                'status': order['status'],
                'payment_status': order['payment_status']
            })
        for detail in order['detail']:
            action = detail.get('action')
            if action not in ('add', 'delete', 'update'):
                raise Exception(u'操作错误, 只允许添加、删除、和修改')

            if action == 'add':
                DB.session.add(OrderDetailModel(
                    oid=order['oid'],
                    mid=order['mid']
                ))
            elif action == 'delete':
                DB.session.query(OrderDetailModel)\
                    .filter(OrderDetailModel.oid == order['oid'])\
                    .filter(OrderDetailModel.mid == order['mid'])\
                    .delete()
            elif action == 'update':
                DB.session.query(OrderDetailModel) \
                    .filter(OrderDetailModel.oid == order['oid']) \
                    .filter(OrderDetailModel.mid == order['mid']) \
                    .update({
                        'mid': order['mid']
                    })

        DB.session.commit()
    return Response({
        'code': 200,
        'message': 'success'
    }, status=200, content_type='application/json')

