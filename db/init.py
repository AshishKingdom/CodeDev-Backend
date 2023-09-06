import datetime

from sqlalchemy.orm import Session
from typing import Generator
from core.security import get_hashed_password

from db.session import Base, engine, SessionLocal
from db.models.user import Users
from db.models.contest import Contests
from db.models.problem import Problems
from db.models.submission import Submissions

from core.settings import Settings


def init_database() -> None:
    Base.metadata.create_all(engine)

    # Adding admin user to the DB if it does not exists
    db: Session = SessionLocal()
    admin_user = db.query(Users).filter(Users.username == Settings.ADMIN_USERNAME).first()

    if admin_user is None:
        db.add(Users(
            username=Settings.ADMIN_USERNAME,
            password=get_hashed_password(Settings.ADMIN_PASSWORD),
            date_of_join=datetime.datetime.now(),
            is_admin=True,
            is_banned=False
        ))
        db.commit()

    db.close()
