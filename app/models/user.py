from sqlalchemy import Column, String

from db.base import base

Base = base()


def create_user_info_model():
    class UserInfo(Base):
        __tablename__ = "user_info"
        user_firstname = Column(String, primary_key=True)
        user_lastname = Column(String)

    return UserInfo
