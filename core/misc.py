from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from core.settings import Settings
from datetime import datetime

reusesable_oath = OAuth2PasswordBearer(
    tokenUrl='/login',
    scheme_name='JWT'
)


def get_current_userinfo(token: str = Depends(reusesable_oath)) -> dict:
    payload: dict = {}
    try:
        payload = jwt.decode(token, Settings.JWT_ACCESS_KEY, Settings.JWT_ALGORITHM)
        exp_time = payload.get("exp")
        if datetime.fromtimestamp(exp_time) < datetime.now():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Access token expired.",
                headers={"WWW-Authenticate": "Bearer"}
            )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not verify credential",
            headers={"WWW-Authenticate": "Bearer"}
        )

    return payload
