from flask import Blueprint, request, session
from sqlalchemy.exc import SQLAlchemyError
from models.user import User
import utils.return_warp as warp

registered_page = Blueprint('registered', __name__, url_prefix='/registered')


@registered_page.route('/sendCode', methods=['GET'])
def send_code():
    phone = request.args.get('phone')
    if phone is None:
        return warp.fail_warp('params')

    session['phone'] = phone
    session['code'] = 123456

    return warp.success_warp('code has sent')


@registered_page.route('/confirmCode', methods=['GET'])
def confirm_code():
    code = int(request.args.get('code'))
    session_code = session.get('code')

    if session_code is None:
        return warp.fail_warp('no session')

    if code == session_code:
        session['confirm'] = True
        return warp.success_warp('confirm code success')
    else:
        return warp.fail_warp('code error')


@registered_page.route('/setPassword', methods=['GET'])
def set_password():
    confirm = session.get('confirm')
    phone = session.get('phone')
    password = request.args.get('password')

    if confirm:
        return warp.fail_warp('no code')

    if password is None:
        return warp.fail_warp('params error')

    user = User(username=phone, password=password)

    try:
        user.new_user()
        session.clear()
        return warp.success_warp('registered success')
    except SQLAlchemyError as e:
        return warp.fail_warp('registered fail')
