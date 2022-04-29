import os

import pymysql
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

pymysql.install_as_MySQLdb()  # ModuleNotFoundError: No module named 'MySQLdb'
app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(24)
# 使用集成方式处理SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost:3306/flask-api?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  # True: 跟踪数据库的修改，及时发送信号
app.config['SQLALCHEMY_POOL_SIZE'] = 600  # 数据库连接池的大小。默认是数据库引擎的默认值（通常是 5）
# 实例化db对象
db = SQLAlchemy(app)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    from controller.user import *

    app.register_blueprint(user, url_prefix='/api')
    app.run(debug=True, host='127.0.0.1', port=5000)
