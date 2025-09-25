from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta

from app.database import get_db
from app.models import user as user_models
from app.schemas import user as user_schemas
from app.core import security
from app.core.config import settings
from app.schemas.user import UserLogin
router = APIRouter()

@router.post("/register", response_model=user_schemas.UserResponse)
def register(user: user_schemas.UserCreate, db: Session = Depends(get_db)):
    # Verificar se usuário já existe
    db_user = db.query(user_models.User).filter(user_models.User.email == user.email).first()
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email já registrado"
        )
    
    # Criar novo usuário
    hashed_password = security.get_password_hash(user.password)
    db_user = user_models.User(
        email=user.email,
        name=user.name,
        hashed_password=hashed_password,
        is_barber=user.is_barber
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user

@router.post("/login", response_model=user_schemas.Token)
def login(user: UserLogin, db: Session = Depends(get_db)):
    # Verificar usuário e senha
    user_db = security.authenticate_user(db, user.email, user.password)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Criar token de acesso
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}