# coding=utf-8
#

from app.db.models.base import DB
from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime,
    func
)


class UserModel(DB.Model):
    __tablename__ = 'tb_user'
    uid = Column(Integer, primary_key=True)
    username = Column(String)
    mobile = Column(Integer)
    password = Column(String)
    gender = Column(String)
    nickname = Column(String)


class EmployeeModel(DB.Model):
    __tablename__ = 'tb_employee'

    id = Column(Integer, primary_key=True)
    employeename = Column(String)
    gender = Column(String)
    address = Column(String)
    type = Column(String)
    mobile = Column(Integer)
    realname = Column(String)


class MenuModel(DB.Model):
    __tablename__ = 'tb_menu'

    mid = Column(Integer, primary_key=True)
    foodname = Column(String)
    category = Column(String)
    price = Column(Float)
    coupon = Column(Float, default=0.0)
    imagepath = Column(String)
    intro = Column(String)


class OrderModel(DB.Model):
    __tablename__ = 'dt_order'
    id = Column(Integer, primary_key=True)
    oid = Column(String)
    uid = Column(Integer)
    eid = Column(Integer)
    status = Column(String)
    create_time = Column(DateTime, default=func.now())
    update_time = Column(DateTime, default=func.now(), onupdate=func.now())
    comment = Column(String)
    amount = Column(Float)
    payment_status = Column(String)


class OrderDetailModel(DB.Model):
    __tablename__ = 'mp_order_detail'
    id = Column(Integer, primary_key=True)
    oid = Column(Integer)
    mid = Column(Integer)
