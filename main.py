from fastapi import FastAPI
from api import base
from core.settings import Settings
from fastapi.middleware.cors import CORSMiddleware
from db.init import init_database

init_database()

origins = [
    "http://localhost:5173",
    "https://localhost:5173",
    "http://127.0.0.1:5500",
    "https://127.0.0.1:5500"
]

app = FastAPI(title=Settings.PROJECT_NAME, version=Settings.PROJECT_VERSION)
app.include_router(base.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

