from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, date, timedelta
from typing import List

from app.database import get_db
from app.models import appointment as appointment_models, user as user_models
from app.schemas import appointment as appointment_schemas
from app.core import security

router = APIRouter()

@router.get("/appointments/by-date/{target_date}", response_model=List[appointment_schemas.AppointmentResponse])
def get_appointments_by_date(
    target_date: date,
    db: Session = Depends(get_db),
    current_user: user_models.User = Depends(security.get_current_active_user)
):
    if not current_user.is_barber:
        raise HTTPException(status_code=403, detail="Acesso negado")
    
    # Calcular início e fim do dia
    start_datetime = datetime.combine(target_date, datetime.min.time())
    end_datetime = start_datetime + timedelta(days=1)
    
    appointments = db.query(appointment_models.Appointment).filter(
        appointment_models.Appointment.appointment_date >= start_datetime,
        appointment_models.Appointment.appointment_date < end_datetime,
        appointment_models.Appointment.status == "agendado"
    ).all()
    
    return appointments

@router.get("/appointments/by-month/{year}/{month}", response_model=List[appointment_schemas.AppointmentResponse])
def get_appointments_by_month(
    year: int,
    month: int,
    db: Session = Depends(get_db),
    current_user: user_models.User = Depends(security.get_current_active_user)
):
    if not current_user.is_barber:
        raise HTTPException(status_code=403, detail="Acesso negado")
    
    # Calcular início e fim do mês
    start_date = date(year, month, 1)
    if month == 12:
        end_date = date(year + 1, 1, 1)
    else:
        end_date = date(year, month + 1, 1)
    
    start_datetime = datetime.combine(start_date, datetime.min.time())
    end_datetime = datetime.combine(end_date, datetime.min.time())
    
    appointments = db.query(appointment_models.Appointment).filter(
        appointment_models.Appointment.appointment_date >= start_datetime,
        appointment_models.Appointment.appointment_date < end_datetime,
        appointment_models.Appointment.status == "agendado"
    ).all()
    
    return appointments