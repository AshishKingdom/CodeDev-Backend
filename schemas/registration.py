from pydantic import BaseModel, ValidationError, root_validator, EmailStr, Field
from datetime import datetime


class RegistrationForm(BaseModel):
    """
Registration form Schema
"""
    username: str = Field(..., regex=r"\w{1,20}")
    first_name: str = Field(..., regex=r"[a-zA-Z]{1,20}")
    last_name: str = Field(..., regex=r"[a-zA-Z]{1,20}")
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=32)
    cnf_password: str = Field(..., min_length=8, max_length=32)
    college: str = Field(..., regex=r"[a-zA-Z]+")
    date_of_joining: datetime = datetime.now()
    is_admin: bool = False
    is_banned: bool = False
    is_email_verified = False

    @root_validator
    def check_password_match(cls, values):
        if values.get('password') != values.get('cnf_password'):
            raise ValueError("Passwords don't match.")
        return values
