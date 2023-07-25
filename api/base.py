from fastapi import APIRouter

from api.v1 import hello
from api.v1 import register
from api.v1 import login
from api.v1 import me

router = APIRouter()

router.include_router(hello.router)
router.include_router(register.router)
router.include_router(login.router)
router.include_router(me.router)

