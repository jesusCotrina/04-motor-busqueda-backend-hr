from fastapi import FastAPI
from database import engine
from models.clinica import Base as ClinicBase
from models.doctor import Base as DoctorBase
from models.especialidad import Base as SpecialtyBase
from api import search as search_router
from sqlalchemy import text
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai


app = FastAPI(title="Motor de busqueda de clinicas y doctores inteligente")

origins = [
    "http://localhost:3000",
    "http://172.16.80.49:3000",
    "http://127.0.0.1:3000",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,           # Qué dominios pueden llamar al backend
    allow_credentials=True,
    allow_methods=["*"],             # GET, POST, PUT, DELETE...
    allow_headers=["*"],             # Headers permitidos
)

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
