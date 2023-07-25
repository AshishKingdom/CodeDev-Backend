from sqlalchemy import Boolean, Column, String, DATETIME

from db.session import Base, engine


class User(Base):
    __tablename__ = 'users'

    username = Column(String, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, index=True)
    password = Column(String)
    college = Column(String)
    date_of_join = Column(DATETIME)
    is_admin = Column(Boolean, default=False)
    is_banned = Column(Boolean, default=False)
    is_email_verified = Column(Boolean, default=False)


Base.metadata.create_all(engine)
