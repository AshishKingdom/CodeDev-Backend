from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    PROJECT_NAME = "CodeDev Backend"
    PROJECT_VERSION = "[ALPHA]"

    DB_URL = os.getenv("DB_URL")

    JWT_ACCESS_KEY = os.getenv("JWT_ACCESS_KEY")
    JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

    ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")
    ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")
