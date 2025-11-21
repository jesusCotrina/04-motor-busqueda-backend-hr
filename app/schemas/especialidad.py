from pydantic import BaseModel

class SpecialtyOut(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
