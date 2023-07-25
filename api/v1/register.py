from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from schemas.registration import RegistrationForm
from db.session import get_db
from db.models.user import User
from core.security import get_hashed_password

router = APIRouter()


@router.post("/register", tags=["user"])
async def register_user(form: RegistrationForm, db: Session = Depends(get_db)):
    # noinspection PyTypeChecker
    user_exists = db.query(User).filter(User.username == form.username).first()
    if user_exists is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists. Please try different username"
        )
    # noinspection PyTypeChecker
    email_exists = db.query(User).filter(User.email == form.email).first()
    if email_exists is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists. Please try a different email."
        )

    hashed_pwd = get_hashed_password(form.password)
    # ek new entry
    user = User(
        username=form.username,
        first_name=form.first_name,
        last_name=form.last_name,
        email=form.email,
        password=hashed_pwd,
        college=form.college,
        date_of_join=form.date_of_joining,
        is_admin=form.is_admin,
        is_banned=form.is_banned,
        is_email_verified=form.is_email_verified
    )
    db.add(user)
    db.commit()

    return {"status": "ok", "content": "user registered successfully"}
