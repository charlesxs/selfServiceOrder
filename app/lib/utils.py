# coding=utf-8
#

import json
from flask import Response


def jsonify(data, *, status=200, message='success'):
    response = {
        'code': status,
        'message': message,
        'data': data
    }

    return Response(
        response=json.dumps(response),
        status=status,
        content_type='application/json'
    )
