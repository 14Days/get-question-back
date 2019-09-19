from flask import Blueprint, session, request
from app.models.user import User
import app.utils.return_warp as warp

secret_page = Blueprint('secret', __name__, url_prefix='/secret')


@secret_page.before_request
def confirm_user():
    user = session.get('user')

    if user is None:
        return warp.fail_warp('please login')


@secret_page.route('', methods=['POST'])
def change_password():
    username = session.get('user')
    old_password = request.form.get('old_password')
    new_password = request.form.get('new_password')

    if old_password is None or new_password is None or old_password == new_password:
        return warp.fail_warp('params error')

    user = User.check_password(username=username)

    if old_password == user.password:
        User.change_password(username=username, password=new_password)
        session.clear()
        return warp.success_warp('change password success')
    else:
        return warp.fail_warp('old password error')
