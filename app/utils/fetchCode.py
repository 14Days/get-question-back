import requests
import random


def create_code():
    code = ''
    for i in range(4):
        code += str(random.randint(0, 9))
    return code


def fetch_code(phone: str, code: str) -> bool:
    response = requests.post('http://sms_developer.zhenzikj.com/sms/send.do', {
        'appId': '102760',
        'appSecret': 'bb85649d-bd4a-4f48-9c0e-57e4d7c30855',
        'message': '欢迎注册题目生成器，您的注册验证码为:{0}'.format(code),
        'number': phone
    })

    result = response.json()

    if result['code'] == 0:
        return True
    else:
        return False
