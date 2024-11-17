from sqlalchemy import Column, String

from app.db.base import base


def create_user_info_model():

    class UserInfo(base):
        __tablename__ = "user_info"
        user_firstname = Column(String, primary_key=True)
        user_lastname = Column(String)

    return UserInfo
