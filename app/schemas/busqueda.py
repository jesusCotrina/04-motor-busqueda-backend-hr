from pydantic import BaseModel

class FiltrosBusqueda(BaseModel):
    nombre_doctor: str | None = None
    especialidad_id: int | None = None
    clinica_id: int | None = None
    distrito: str | None = None
    dia: str | None = None
    tipo_atencion: str | None = None
