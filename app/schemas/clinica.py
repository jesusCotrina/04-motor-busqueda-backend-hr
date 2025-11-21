from pydantic import BaseModel

class ClinicOut(BaseModel):
    id: int
    name: str
    address: str | None

    class Config:
        orm_mode = True
