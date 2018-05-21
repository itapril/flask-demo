from flask import jsonify,make_response


def base_resp(message, result, status=True, error_code=0, status_code=200):
    """
    :param message:提示信息
    :param result: 返回的对象
    :param status: 状态值
    :param error_code: 错误code
    :param status_code: 状态码
    :return:
    """
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
