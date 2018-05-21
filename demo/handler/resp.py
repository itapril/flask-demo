import json
from flask import jsonify,make_response


def base_resp(message, result, status=True, error_code=0, status_code=200):
    resp = {
        'status': True,
        'errorCode': 0,
        'message': '',
        'result': {},
    }
    resp['message'] = message
    resp['result'] = result
    resp['status'] = status
    resp['errorCode'] = error_code
    # response_str = json.dumps(resp, sort_keys=False)
    response = make_response(jsonify(resp), status_code)
    return response
