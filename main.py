from fastapi import FastAPI
from api import base
from core.settings import Settings
from db.init import init_database

init_database()

app = FastAPI(title=Settings.PROJECT_NAME, version=Settings.PROJECT_VERSION)
app.include_router(base.router)

