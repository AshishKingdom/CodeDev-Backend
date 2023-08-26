from fastapi import APIRouter, Depends, HTTPException, status
from db.models.user import Users
from sqlalchemy.orm import Session
from db.session import get_db
from core.misc import get_current_userinfo

router = APIRouter()


@router.get("/me")
def get_me(userinfo: dict = Depends(get_current_userinfo), db: Session = Depends(get_db)):
    if userinfo is None:
        return {"msg": "no user logined"}

    # noinspection PyTypeChecker
    curr_user: str = userinfo.get('user')
    user_info = db.query(Users).filter(Users.username == curr_user)
    print(curr_user)
    return {"yo":"yo"}
