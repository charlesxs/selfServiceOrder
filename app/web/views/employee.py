# coding=utf-8
#

from flask import Blueprint
from flask import request, Response
from flask import session
from app.db.models.tables import EmployeeModel
from app.db.models.base import DB

bp = Blueprint('employee', __name__)


@bp.route('/employee', methods=['GET'])
def list_employee():
    if not session.get('is_login'):
        return Response({
            'code': 403,
            'message': 'require login'
        }, status=403, content_type='application/json')

    models = EmployeeModel.query.all()

    json_models = [{
        'id': m.id,
        'name': m.employeename,
        'gender': m.gender,
        'address': m.address,
        'type': m.type,
        'mobile': m.mobile,
        'realname': m.realname
    } for m in models]

    return Response({
        'code': 200,
        'message': 'success',
        'data': json_models
    }, status=200, content_type='application/json')


@bp.route('/delete_employee', methods=['POST'])
def delete_employee():
    if not session.get('is_login'):
        return Response({
            'code': 403,
            'message': 'require login'
        }, status=403, content_type='application/json')

    delete_employee_ids = request.json.get('delete_ids')

    DB.session.begin()
    for id_ in delete_employee_ids:
        em = EmployeeModel.query.filter(EmployeeModel.id == id_).first()
        if em is None:
            continue

        DB.session.delete(em)
    DB.session.commit()
    return Response({
        'code': 200,
        'message': 'success'
    }, status=200, content_type='application/json')


@bp.route('/update_employee', methods=['POST'])
def update_employee():
    """
    只允许修改 地址、电话和职位
    :return:
    """
    if not session.get('is_login'):
        return Response({
            'code': 403,
            'message': 'require login'
        }, status=403, content_type='application/json')

    employee_info = request.json.get('employee_info')

    DB.session.begin()
    DB.session.query(EmployeeModel)\
        .filter(EmployeeModel.id == employee_info['id'])\
        .update({
            'address': employee_info['address'],
            'type': employee_info['type'],
            'mobile': employee_info['mobile']
        })
    DB.session.commit()
    return Response({
        'code': 200,
        'message': 'success'
    }, status=200, content_type='application/json')
