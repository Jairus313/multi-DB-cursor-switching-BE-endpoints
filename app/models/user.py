from sqlalchemy import Column, String
from app.db.base import Base


class User(Base):
    __tablename__ = "user_table"

    user_name = Column(String, primary_key=True)
    user_db_url = Column(String)
    user_db_host = Column(String)
    user_db_name = Column(String)
    user_db_username = Column(String)
    user_db_password = Column(String)
