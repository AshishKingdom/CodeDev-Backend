from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    PROJECT_NAME = "CodeDev Backend"
    PROJECT_VERSION = "[ALPHA]"

    DB_URL = os.getenv("DB_URL")

    JWT_ACCESS_KEY = os.getenv("JWT_ACCESS_KEY")
    JWT_REFRESH_KEY = os.getenv("JWT_REFRESH_KEY")
    JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
    REFRESH_TOKEN_EXPIRE_MINUTES = int(os.getenv("REFRESH_TOKEN_EXPIRE_MINUTES"))
    ORIGINS = os.getenv("ORIGINS").split(',')
