from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime, time
import re

from app.database import get_db
from app.models import appointment as appointment_models, user as user_models
from app.schemas import appointment as appointment_schemas
from app.core import security

router = APIRouter()

def is_valid_time_slot(appointment_time: datetime):
    """Verifica se o horário está em intervalos de 30 minutos"""
    return appointment_time.minute % 30 == 0

def is_time_available(db: Session, appointment_time: datetime, duration: int):
    """Verifica se o horário está disponível"""
    end_time = appointment_time + time(minutes=duration)
    
    # Verificar conflitos de agendamento
    conflicting_appointments = db.query(appointment_models.Appointment).filter(
        appointment_models.Appointment.appointment_date < end_time,
        appointment_models.Appointment.appointment_date + 
        (appointment_models.Appointment.duration * time(minutes=1)) > appointment_time,
        appointment_models.Appointment.status == "agendado"
    ).all()
    
    return len(conflicting_appointments) == 0

@router.post("/", response_model=appointment_schemas.AppointmentResponse)
def create_appointment(
    appointment: appointment_schemas.AppointmentCreate,
    db: Session = Depends(get_db),
    current_user: user_models.User = Depends(security.get_current_active_user)
):
    # Verificar se o horário está em intervalos de 30 minutos
    if not is_valid_time_slot(appointment.appointment_date):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Os agendamentos devem ser em intervalos de 30 minutos (ex: 09:00, 09:30, 10:00)"
        )
    
    # Verificar se o horário está disponível
    if not is_time_available(db, appointment.appointment_date, appointment.duration):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Já existe um agendamento para este horário"
        )
    
    # Criar o agendamento
    db_appointment = appointment_models.Appointment(
        **appointment.dict(),
        user_id=current_user.id
    )
    
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    
    return db_appointment

@router.delete("/{appointment_id}")
def delete_appointment(
    appointment_id: int,
    db: Session = Depends(get_db),
    current_user: user_models.User = Depends(security.get_current_active_user)
):
    db_appointment = db.query(appointment_models.Appointment).filter(
        appointment_models.Appointment.id == appointment_id
    ).first()
    
    if not db_appointment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Agendamento não encontrado"
        )
    
    # Verificar se o usuário é o dono do agendamento ou um barbeiro
    if db_appointment.user_id != current_user.id and not current_user.is_barber:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Você não tem permissão para cancelar este agendamento"
        )
    
    # Marcar como cancelado em vez de deletar
    db_appointment.status = "cancelado"
    db.commit()
    
    return {"message": "Agendamento cancelado com sucesso"}