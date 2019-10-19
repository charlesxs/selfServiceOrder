# coding=utf-8
#

from __future__ import division
from datetime import datetime, timedelta
from flask import Blueprint
from flask import request, Response
from flask import session
from sqlalchemy import func
from app.db.models.tables import OrderModel, OrderDetailModel, MenuModel, UserModel
from app.db.models.base import DB
from app.lib.utils import jsonify

bp = Blueprint('statistics', __name__)


@bp.route('/hot_food', methods=['GET'])
def hot_food():
    """
    统计所选月份Top10 热门食物
    :return:
    """
    month = int(request.args.get('month'))
    start_time = datetime(year=datetime.now().year, month=month, day=1)
    end_time = datetime(year=datetime.now().year, month=month + 1, day=1)
    # 最高热度是5
    hot_rate = 5
    models = DB.session.query(OrderDetailModel.mid, func.count(OrderDetailModel.id).label('count'))\
        .join(OrderModel, OrderModel.id == OrderDetailModel.oid)\
        .filter(OrderModel.create_time >= start_time)\
        .filter(OrderModel.create_time < end_time)\
        .group_by(OrderDetailModel.mid)\
        .order_by(func.count(OrderDetailModel.id).desc())\
        .limit(10)\
        .all()

    if not models:
        return jsonify([])

    count_map = {m.mid: m.count for m in models}
    # 计算 从被点次数 -> 热度的 映射因子
    mapping_factor = hot_rate / max(count_map.values())
    food_models = MenuModel.query.filter(MenuModel.mid.in_([m.mid for m in models])).all()
    result = [dict(
        id=food.mid,
        name=food.foodname,
        imagePath=food.imagepath,
        intro=food.intro,
        category=food.category,
        price=food.price,
        count=count_map[food.mid],
        rate=round(count_map[food.mid] * mapping_factor, 2)
    ) for food in food_models]

    return jsonify(result)


@bp.route('/cash_flow', methods=['GET'])
def cash_flow():
    """
    统计/打印 所选月份流水及明细
    :return:
    """
    month = int(request.args.get('month'))
    start_time = datetime(year=datetime.now().year, month=month, day=1)
    end_time = datetime(year=datetime.now().year, month=month + 1, day=1)
    date_fmt = '%Y-%m-%d %H:%M:%S'

    models = OrderModel.query\
        .filter(OrderModel.create_time >= start_time)\
        .filter(OrderModel.create_time < end_time)\
        .all()

    orders = []
    for m in models:
        order = {
            'oid': m.oid,
            'status': m.status,
            'create_time': m.create_time.strftime(date_fmt),
            'update_time': m.update_time.strftime(date_fmt),
            'comment': m.comment,
            'amount': m.amount,
            'payment': m.payment_status
        }

        user = UserModel.query\
            .filter(UserModel.uid == m.uid)\
            .first()
        order['username'] = user.nickname
        orders.append(order)
    return jsonify(orders)
