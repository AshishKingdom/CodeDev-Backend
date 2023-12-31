from fastapi import APIRouter

from api.v1 import hello
from api.v1 import register
from api.v1 import login
from api.v1 import me
from api.v1 import create_contest
from api.v1 import contest

router = APIRouter(prefix="/api")

router.include_router(hello.router)
router.include_router(register.router)
router.include_router(login.router)
router.include_router(me.router)
router.include_router(create_contest.router)
router.include_router(contest.router)

