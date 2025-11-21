from fastapi import FastAPI
from database import engine
from models.clinica import Base as ClinicBase
from models.doctor import Base as DoctorBase
from models.especialidad import Base as SpecialtyBase
from api import search as search_router
from sqlalchemy import text

app = FastAPI(title="Motor de busqueda de clinicas y doctores inteligente")

app.include_router(search_router.router)

@app.on_event("startup")
async def startup_db_verify():
    try:
        async with engine.begin() as conn:
            await conn.execute(text("SELECT 1"))
        print("DB connection OK")
    except Exception as e:
        print("Database connection failed:", e)
        raise e
