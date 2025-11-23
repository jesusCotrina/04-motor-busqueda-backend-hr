import os
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
import google.generativeai as genai
import asyncio
import json
from concurrent.futures import ThreadPoolExecutor
import os,time
from google.cloud import secretmanager


def get_secret(secret_name: str):
    client = secretmanager.SecretManagerServiceClient()
    project_id = "TU_PROJECT_ID"
    name = f"projects/138784101658/secrets/API_KEY_GEN/versions/latest"
    response = client.access_secret_version(name=name)
    return response.payload.data.decode("utf-8")

API_KEY_GEN = get_secret("API_KEY_GEN")

executor = ThreadPoolExecutor()

genai.configure(api_key=API_KEY_GEN)

model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    generation_config={
        "response_mime_type": "application/json"
    }
)

# Ruta al directorio /sql
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SQL_DIR = os.path.join(BASE_DIR, "sql")
PROMPT_DIR = os.path.join(BASE_DIR, "propmt")

async def load_prompt(filename: str) -> str:
    path = os.path.join(PROMPT_DIR, filename)
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
    

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
    sql = await load_sql("busqueda_maestro.sql")
    params = {
        "nombre_doctor": filters.nombre_doctor,
        "especialidad_id": filters.especialidad_id,
        "clinica_id": filters.clinica_id,
        "distrito": filters.distrito,
        "dia": filters.dia,
        "tipo_atencion": filters.tipo_atencion
    }
    print(params)
    result = await db.execute(text(sql), params)
    return result.mappings().all()

async def consulta_medicamentos_(db:AsyncSession ,especialidad_ids):
    sql = await load_sql("busqueda_medicamentos.sql")
    result = await db.execute(text(sql), {"especialidad_ids": especialidad_ids.especialidad_ids})
    return result.mappings().all()


async def consulta_x_dolencia(db:AsyncSession ,especialidades):
    sql = await load_sql("busqueda_x_dolencia_maestro.sql")
    result = await db.execute(text(sql), {"especialidades_nombre": especialidades})
    return result.mappings().all()

async def consulta_busqueda_semantica(db:AsyncSession, filtros):
    sql = await load_sql("busqueda_semantica_maestro.sql")
    print("filtro consulta",filtros)
    params = {
        "nombre_doctor": filtros["nombre_doctor"],
        "especialidad_nombre": filtros["especialidad"],
        "clinica_nombre": filtros["clinica"],
        "distrito": filtros["distrito"],
        "dia": filtros["dia"],
        "tipo_atencion": filtros["tipo_atencion"]
    }
    result = await db.execute(text(sql), params)
    return result.mappings().all()

async def consulta_medicamentos_x_dolencia(db:AsyncSession, especialidades):
    sql = await load_sql("busqueda_medicamentos_x_dolencia.sql")
    result = await db.execute(text(sql), {"especialidades_nombre": especialidades})
    return result.mappings().all()

async def consulta_semantica(db:AsyncSession ,user_input):
    prompt = await load_prompt("busqueda_semantica.txt")
    prompt=prompt.replace("{user_input}",user_input.texto)
    
    start = time.perf_counter()
    

    loop = asyncio.get_running_loop()
    response = await loop.run_in_executor(
        executor,
        lambda: model.generate_content(
            contents=[{"parts": [{"text": prompt}]}],
            generation_config={"response_mime_type": "application/json"}
        )
    )
    end = time.perf_counter()
    elapsed_ms = round((end - start) * 1000, 2)
    print("tiempo consulta llm:",elapsed_ms)

    json_llm=json.loads(response.text)
    print("json_llm",json_llm)

    start = time.perf_counter()
    if json_llm["tipo"]=="dolencia":
        print("buscando por dolencia")
        data = await consulta_x_dolencia(db,json_llm["especialidades"])
        medicamentos_info = await consulta_medicamentos_x_dolencia(db,json_llm["especialidades"])
        json_llm["data"]=data
        json_llm["medicamentos"]=medicamentos_info

        end = time.perf_counter()
        elapsed_ms = round((end - start) * 1000, 2)
        print("tiempo consulta base de datos semantica:",elapsed_ms)

        return json_llm

    elif json_llm["tipo"]=="busqueda":
        print("buscando por busqueda")
        data = await consulta_busqueda_semantica(db, json_llm["filtros_busqueda"])
        json_llm["data"]=data
        end = time.perf_counter()
        elapsed_ms = round((end - start) * 1000, 2)
        print("tiempo consulta base de datos semantica:",elapsed_ms)
        return json_llm

    elif json_llm["tipo"] is None or json_llm["tipo"]=="null":
        print("busqueda null")
        return json_llm
