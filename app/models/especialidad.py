from sqlalchemy import Column, Integer, String
from models.clinica import Base

class Specialty(Base):
    __tablename__ = "especialidades"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
