from datetime import datetime, timedelta
from jose import jwt
from core.settings import Settings
from typing import Dict
import bcrypt


def get_access_token(data: Dict, expire_time: int | timedelta = None, is_refresh_token: bool = False) -> str:
    if expire_time is not None:
        expire_time = datetime.utcnow() + expire_time
    else:
        if is_refresh_token:
            expire_time = datetime.utcnow() + timedelta(minutes=Settings.REFRESH_TOKEN_EXPIRE_MINUTES)
        else:
            expire_time = datetime.utcnow() + timedelta(minutes=Settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = data.copy()
    to_encode.update({"exp": expire_time})

    if is_refresh_token:
        token = jwt.encode(to_encode, Settings.JWT_REFRESH_KEY, algorithm=Settings.JWT_ALGORITHM)
    else:
        token = jwt.encode(to_encode, Settings.JWT_ACCESS_KEY, algorithm=Settings.JWT_ALGORITHM)
    return token


def get_hashed_password(password: str) -> bytes:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def verify_password(password: bytes, hashed_password: bytes) -> bool:
    return bcrypt.checkpw(password, hashed_password)
