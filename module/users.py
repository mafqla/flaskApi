
from sqlalchemy import Table

from conmon.db import dbconnect

dbsession, md, DBase = dbconnect()


class Users(DBase):
    __table__ = Table('users', md, autoload=True)

    # 查询用户
    def find_by_username(self, username):
        result = dbsession.query(Users).filter_by(username=username).all()
        return result

    def find_by_userid(self, id):
        user = dbsession.query(Users).filter_by(id=id).one()
        return user
    
    # 用户注册
    def register(self, username, password):
        user = Users(username=username, password=password)
        dbsession.add(user)
        dbsession.commit()
        return user
