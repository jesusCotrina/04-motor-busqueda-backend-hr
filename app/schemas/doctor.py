from pydantic import BaseModel
from schemas.clinica import ClinicOut

class DoctorOut(BaseModel):
    id: int
    name: str
    clinic: ClinicOut | None

    class Config:
        orm_mode = True
