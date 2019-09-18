from flask import Blueprint, request
from models.user import User
import utils.return_warp as warp

login_out_page = Blueprint('login_out', __name__, url_prefix='/log')


@login_out_page.route('/in', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    # 校验必须参数
    if username is None or password is None:
        return warp.fail_warp('params error')

    user = User.check_password(username=username)

    if user.password == password:
        return warp.success_warp('login success')
    else:
        return warp.fail_warp('user error')
