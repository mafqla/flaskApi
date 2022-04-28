import hashlib

from flask import Blueprint, request, session, jsonify, make_response

from module.users import Users

user = Blueprint('user', __name__)


# 注册

@user.route('/register', methods=['POST'])
def register():
    user = Users()
    username = request.form.get('username').strip()
    password = request.form.get('password').strip()

    if len(password) < 5:
        return '密码不能少于6为'
    elif len(user.find_by_username(username)) > 0:
        return '用户已经注册'
    else:
        password = hashlib.md5(password.encode()).hexdigest()
        result = user.register(username, password)
        session['id'] = result.id
        session['username'] = username

        return jsonify('注册成功')


@user.route('/login', methods=['POST'])
def login():
    user = Users()
    username = request.form.get('username').strip()
    password = request.form.get('password').strip()

    # 实现登录功能
    password = hashlib.md5(password.encode()).hexdigest()
    result = user.find_by_email(username)
    if len(result) == 1 and result[0].password == password:
        session['userid'] = result[0].userid
        session['username'] = username
        # 将Cookie写入浏览器
        response = make_response('login-pass')
        response.set_cookie('username', username, max_age=30 * 24 * 3600)
        response.set_cookie('password', password, max_age=30 * 24 * 3600)

        return response
    else:
        return 'login-fail'
