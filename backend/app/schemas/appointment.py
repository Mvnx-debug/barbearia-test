from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AppointmentBase(BaseModel):
    customer_name: str
    service: str
    appointment_date: datetime
    duration: int = 30

class AppointmentCreate(AppointmentBase):
    pass

class AppointmentResponse(AppointmentBase):
    id: int
    user_id: int
    status: str
    
    class Config:
        from_attributes = True