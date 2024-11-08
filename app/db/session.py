from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import DBConfig


engine = create_engine(DBConfig.database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
