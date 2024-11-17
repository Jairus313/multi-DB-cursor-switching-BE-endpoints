from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import DBConfig


engine = create_engine(DBConfig.database_url)
MasterSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_user_db_session(user_db_url):
    engine = create_engine(user_db_url)
    session_local = sessionmaker(bind=engine)

    return session_local
