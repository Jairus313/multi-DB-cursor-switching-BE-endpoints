from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import text

from app.db.session import MasterSession, get_user_db_session
from app.models.master import User as MasterUser
from app.models.user import create_user_info_model

router = APIRouter()


@router.get("/user/{user_name}")
def get_user_info(user_name: str):
    master_session = MasterSession()

    user_entry = (
        master_session.query(MasterUser)
        .filter(MasterUser.user_name == user_name)
        .first()
    )

    if not user_entry:
        raise HTTPException(status_code=404, detail="User not found in Master DB")

    user_db_url = f"postgresql://{user_entry.user_db_username}:{user_entry.user_db_password}@localhost/{user_entry.user_db_name}"
    user_db_session = get_user_db_session(user_db_url)()

    user_info_model = create_user_info_model()
    user_info = user_db_session.query(user_info_model).first()

    if not user_info:
        raise HTTPException(status_code=404, detail="User info not found in User DB")

    return {
        "user_firstname": user_info.user_firstname,
        "user_lastname": user_info.user_lastname,
    }
