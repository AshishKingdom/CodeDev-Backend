from pydantic import BaseModel, ValidationError, validator
from datetime import datetime


class RegistrationForm(BaseModel):
    """
Registration form Schema
"""
    username: str
    first_name: str
    last_name: str
    email: str
    password: str
    cnf_password:str
    college: str = None
    date_of_joining: datetime = datetime.now()
    is_admin: bool = False
    is_banned: bool = False
    is_email_verified = False
