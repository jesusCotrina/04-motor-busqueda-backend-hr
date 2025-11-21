from pydantic import BaseModel
from typing import List

class EspecialidadMedicamentos(BaseModel):
    especialidad_ids: List[int]  
