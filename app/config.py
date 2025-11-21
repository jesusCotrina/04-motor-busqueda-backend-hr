import os
from dotenv import load_dotenv

load_dotenv()  # opcional si usas archivo .env

class Settings:
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL", "postgresql+asyncpg://jcotrina:qZBwMl5rRWt6O7qI6MZOqdlu650hiHy4@dpg-d4ftj73e5dus739f1j50-a.virginia-postgres.render.com/motor_busqueda"
    )
    SECRET_KEY: str = os.getenv("SECRET_KEY", "default_secret_key")

settings = Settings()