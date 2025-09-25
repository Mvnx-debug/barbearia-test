from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Appointment(Base):
    __tablename__ = "appointments"
    
    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String, nullable=False)
    service = Column(String, nullable=False)
    appointment_date = Column(DateTime, nullable=False)
    duration = Column(Integer, default=30)
    user_id = Column(Integer, ForeignKey("users.id"))  # Deve corresponder ao __tablename__ de User
    status = Column(String, default="agendado")
    
    user = relationship("User")