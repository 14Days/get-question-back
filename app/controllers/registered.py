from flask import Blueprint, request, session
from sqlalchemy.exc import SQLAlchemyError
from app.models.user import User
import app.utils.return_warp as warp
from app.utils.fetchCode import create_code, fetch_code

registered_page = Blueprint('registered', __name__, url_prefix='/registered')


@registered_page.route('/sendCode', methods=['GET'])
def send_code():
    phone = request.args.get('phone')
    if phone is None:
        return warp.fail_warp('params error')
    user = User.check_password(phone)
    if user is not None:
        return warp.fail_warp('user exist')

    code = create_code()
    result = fetch_code(phone=phone, code=code)
    if result:
        session['phone'] = phone
        session['code'] = code
        return warp.success_warp('code has sent')
    else:
        return warp.fail_warp('code send fail')


@registered_page.route('/confirmCode', methods=['GET'])
def confirm_code():
    code = request.args.get('code')
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
