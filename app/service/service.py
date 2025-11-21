import os
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

# Ruta al directorio /sql
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SQL_DIR = os.path.join(BASE_DIR, "sql")

async def load_sql(filename: str) -> str:
    path = os.path.join(SQL_DIR, filename)
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

async def get_filtros_metadata(db: AsyncSession):
    sql = await load_sql("metadata_filtro.sql")
    result = await db.execute(text(sql))
    row = result.fetchone()
    return row[0]   # JSON result


async def get_datos(db:AsyncSession ,filters):
    sql = await load_sql("busqueda.sql")
    params = {
        "nombre_doctor": filters.nombre_doctor,
        "especialidad_id": filters.especialidad_id,
        "clinica_id": filters.clinica_id,
        "distrito": filters.distrito,
        "dia": filters.dia,
        "tipo_atencion": filters.tipo_atencion
    }
    result = await db.execute(text(sql), params)
    return result.mappings().all()