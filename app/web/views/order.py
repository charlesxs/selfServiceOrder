# coding=utf-8
#

from datetime import datetime
from flask import Blueprint
from flask import request, Response
from app.db.models.tables import OrderModel, OrderDetailModel, MenuModel, UserModel
from app.db.models.base import DB
from app.lib.utils import jsonify

bp = Blueprint('order', __name__)


@bp.route('/generate_order', methods=['POST'])
def generate_order():
    data = request.json.get('data')
    # 验证user
    um = UserModel.query.filter(
        UserModel.username == data['username']
    ).first()
    if not um:
        return Response({
            'code': 400,
            'message': 'user not exists'
        }, status=400, content_type='application/json')

    # 生成订单
    order = OrderModel(
        oid=data['id'],
        status=u'已下单',
        create_time=datetime.now(),
        update_time=datetime.now(),
        amount=data['amount'],
        uid=um.uid,
        payment_status='已支付'
    )
    # 写入DB
    DB.session.begin(subtransactions=True)
    DB.session.add(order)
    DB.session.commit()

    # 写订单详情表
    for food in data['detail']:
        DB.session.begin(subtransactions=True)
        DB.session.add(OrderDetailModel(
            oid=order.id,
            mid=food['id']
        ))
        DB.session.commit()
    return Response({
        'code': 200,
        'message': 'success'
    }, status=200, content_type='application/json')


@bp.route('/list_orders', methods=['GET'])
def order():
    orders = OrderModel.query.order_by(OrderModel.create_time.desc()).all()
    date_fmt = '%Y-%m-%d %H:%M:%S'
    result = []
    for o in orders:
        user = UserModel.query.filter(UserModel.uid == o.uid).first()

        o_map = {
            'id': o.oid,
            'status': o.status,
            'createTime': o.create_time.strftime(date_fmt),
            'updateTime': o.update_time.strftime(date_fmt),
            'comment': o.comment,
            'amount': o.amount,
            'payment': o.payment_status,
            'username': user.nickname
        }

        details_models = DB.session.query(MenuModel)\
            .join(OrderDetailModel, OrderDetailModel.mid == MenuModel.mid)\
            .filter(OrderDetailModel.oid == o.id).all()

        o_map['detail'] = [dict(
            id=d.mid,
            foodname=d.foodname,
            price=d.price,
            imagePath=d.imagepath,
            intro=d.intro,
            category=d.category
        ) for d in details_models]
        result.append(o_map)

    return jsonify(result)


@bp.route('/edit_order', methods=['POST'])
def edit_order():
    order = request.json.get('data')
    om = OrderModel.query\
        .filter(OrderModel.oid == order['id'])\
        .first()

    if not om:
        return jsonify({}, 400, message='not found order')

    with DB.session.begin(subtransactions=True):
        DB.session.query(OrderModel)\
            .filter(OrderModel.oid == order['id'])\
            .update({
                'amount': order['amount'],
                'status': order['status'],
                'payment_status': order['payment'],
                'update_time': datetime.now(),
            })

        mids = {d['id'] for d in order['detail']}
        q = DB.session.query(OrderDetailModel)\
            .filter(OrderDetailModel.oid == om.id)
        old_ids = {x.mid for x in q}

        delete_list = list(old_ids.difference(mids))
        add_list = list(mids.difference(old_ids))

        if delete_list:
            q = DB.session.query(OrderDetailModel)\
                .filter(OrderDetailModel.oid == om.id)\
                .filter(OrderDetailModel.mid.in_(delete_list))
            [DB.session.delete(x) for x in q]

        for x in add_list:
            DB.session.add(OrderDetailModel(
                oid=om.id,
                mid=x
            ))

    return jsonify({'data': 'ok'})

