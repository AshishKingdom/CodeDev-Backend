from fastapi import APIRouter, Depends, HTTPException, status
from db.models.user import User
from sqlalchemy.orm import Session
from db.session import get_db
from core.misc import get_current_user

router = APIRouter()


@router.get("/me")
def get_me(curr_user: str = Depends(get_current_user), db: Session = Depends(get_db)):
    if curr_user is None:
        return {"mess": "no user logined"}

    # noinspection PyTypeChecker
    user_info = db.query(User).filter(User.username == curr_user)
    print(curr_user)
    return {"yo":"yo"}
