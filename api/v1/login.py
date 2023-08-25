from fastapi import APIRouter, status, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from db.session import get_db
from db.models.user import Users
from core.security import verify_password, get_access_token
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/login", tags=['user'])
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # noinspection PyTypeChecker
    user = db.query(Users).filter(Users.username == form_data.username).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid username/password"
        )

    hashed_pass = user.password
    if not verify_password(form_data.password.encode('utf-8'), hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid username/password"
        )

    return {"access_token": get_access_token({"user": user.username}), "is_admin": user.is_admin}
