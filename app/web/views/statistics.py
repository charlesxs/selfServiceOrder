# coding=utf-8
#

from datetime import datetime, timedelta
from flask import Blueprint
from flask import request, Response
from flask import session
from sqlalchemy import func
from app.db.models.tables import OrderModel, OrderDetailModel, MenuModel
from app.db.models.base import DB

bp = Blueprint('statistics', __name__)


@bp.route('/hot_food', methods=['GET'])
def hot_food():
    """
    统计所选月份Top10 热门食物
    :return:
    """
    if not session.get('is_login'):
        return Response({
            'code': 403,
            'message': 'require login'
        }, status=403, content_type='application/json')

    month = request.args.get('month')
    start_time = datetime(year=datetime.now().year, month=month, day=1)
    end_time = start_time + timedelta(weeks=1)

    models = DB.session.query(OrderDetailModel.mid, func.count(OrderDetailModel.id).label('count'))\
        .join(OrderModel, OrderModel.old == OrderDetailModel.oid)\
        .filter(OrderModel.create_time >= start_time)\
        .filter(OrderModel.create_time < end_time)\
        .group_by(OrderDetailModel.mid)\
        .order_by(func.count(OrderDetailModel.id).desc())\
        .limit(10)\
        .all()

    food_models = MenuModel.query.filter(MenuModel.mid.in_([m.mid for m in models])).all()
    result = [dict(
        id=food.id,
        name=food.name,
        imgPath=food.imgPath,
        intro=food.intro,
        category=food.category,
        price=food.price
    ) for food in food_models]

    return Response({
        'code': 200,
        'message': 'success',
        'data': result
    }, status=200, content_type='application/json')


@bp.route('/cash_flow', methods=['GET'])
def cash_flow():
    """
    统计/打印 所选月份流水及明细
    :return:
    """
    if not session.get('is_login'):
        return Response({
            'code': 403,
            'message': 'require login'
        }, status=403, content_type='application/json')
    month = request.args.get('month')
    start_time = datetime(year=datetime.now().year, month=month, day=1)
    end_time = start_time + timedelta(weeks=1)

    models = OrderModel.query\
        .filter(OrderModel.create_time >= start_time)\
        .filter(OrderModel.create_time < end_time)\
        .all()

    total_amount, orders = 0, []
    for m in models:
        total_amount += m.amount
        orders.append({
            'oid': m.oid,
            'status': m.status,
            'create_time': m.create_time,
            'update_time': m.update_time,
            'comment': m.comment,
            'amount': m.amount,
            'payment_status': m.payment_status
        })

    return Response({
        'code': 200,
        'message': 'success',
        'data': {'total_amount': total_amount, 'orders': orders}
    }, status=200, content_type='application/json')
