from pydantic import BaseSettings
from typing import Optional
import os
from dotenv import load_dotenv


class Settings(BaseSettings):
    app_name: str = "Ounass Marketing Case Study"
    admin_email: str = "admin"
    items_per_user: int = 50
    allowed_origins: str | None = None

    class Config:
        env_file = './.env'


load_dotenv()

APP_ID = os.getenv('APP_ID')
APP_SECRET = os.getenv('APP_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCOUNT_ID = os.getenv('ACCOUNT_ID')
PAGE_ID = os.getenv('PAGE_ID')

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
