import os
from dotenv import load_dotenv

load_dotenv()  # opcional si usas archivo .env

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL", "")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "default_secret_key")

settings = Settings()