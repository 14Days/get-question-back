from flask import jsonify


def success_warp(data=None) -> str:
    if data is None:
        data = {}
    return jsonify({
        'status': 'success',
        'data': data
    })


def fail_warp(msg: str) -> str:
    return jsonify({
        'status': 'error',
        'err_msg': msg
    })
