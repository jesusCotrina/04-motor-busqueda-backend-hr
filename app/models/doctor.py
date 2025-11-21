from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.clinica import Base

class Doctor(Base):
    __tablename__ = "doctor"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    clinic_id = Column(Integer, ForeignKey("clinics.id"))
    specialty_id = Column(Integer, ForeignKey("specialties.id"))

    clinic = relationship("Clinic")
