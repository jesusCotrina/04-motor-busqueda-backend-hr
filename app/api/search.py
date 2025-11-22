from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from database import get_db
from models.clinica import Clinica
from models.doctor import Doctor
from models.especialidad import Specialty
from schemas.clinica import ClinicOut
from schemas.doctor import DoctorOut
from schemas.especialidad import SpecialtyOut
from schemas.busqueda import FiltrosBusqueda
from schemas.user_input import UserInput
from schemas.medicamentos import EspecialidadMedicamentos
from service.service import get_filtros_metadata,get_datos,consulta_semantica,consulta_medicamentos_
import time 

router = APIRouter(prefix="/search", tags=["search"])


@router.get("/metadata/filtros")
async def filtros_metadata(db: AsyncSession = Depends(get_db)):
    """
    Devuelve: especialidades, clínicas, sedes, tipos_atencion.
    Todo en una sola consulta SQL.
    """
    start = time.perf_counter()
    data= await get_filtros_metadata(db)
    end = time.perf_counter()
    elapsed_ms = round((end - start) * 1000, 2)
    print("tiempo consulta metadata",elapsed_ms)
    return data

@router.post("/busqueda")
async def busqueda(filters: FiltrosBusqueda, db: AsyncSession = Depends(get_db)):
    """
    Devuelve: especialidades, clínicas, sedes, tipos_atencion.
    Todo en una sola consulta SQL.
    """
    start = time.perf_counter()

    data= await get_datos(db,filters)

    end = time.perf_counter()
    elapsed_ms = round((end - start) * 1000, 2)
    print("tiempo consulta busqueda",elapsed_ms)
    return data

@router.post("/busqueda_semantica")
async def busqueda_semantica(user_input: UserInput,db: AsyncSession = Depends(get_db)):
    start = time.perf_counter()
    data= await consulta_semantica(db,user_input)
    end = time.perf_counter()
    elapsed_ms = round((end - start) * 1000, 2)
    print("tiempo consulta busqueda_semantica",elapsed_ms)

    return data


@router.get("/detalle_doctor")
async def detalle_doctor(db: AsyncSession = Depends(get_db)):
    """
    Devuelve: especialidades, clínicas, sedes, tipos_atencion.
    Todo en una sola consulta SQL.
    """
    start = time.perf_counter()
    data= await get_filtros_metadata(db)
    end = time.perf_counter()
    elapsed_ms = round((end - start) * 1000, 2)
    print("tiempo consulta detalle_doctor",elapsed_ms)
    return data


@router.post("/busqueda_medicamentos")
async def consulta_medicamentos(EspecialidadMedicamento: EspecialidadMedicamentos,db: AsyncSession = Depends(get_db)):
    start = time.perf_counter()
    print("busqueda_medicamentos",EspecialidadMedicamento)
    data= await consulta_medicamentos_(db,EspecialidadMedicamento)
    end = time.perf_counter()
    elapsed_ms = round((end - start) * 1000, 2)
    print("tiempo consulta busqueda_medicamentos",elapsed_ms)

    return data
