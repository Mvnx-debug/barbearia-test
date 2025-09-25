from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine, Base

# Importar os modelos para que sejam registrados
import app.models.user
import app.models.appointment

# Criar todas as tabelas de uma vez
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Barbearia API", version="1.0.0")

# Configuração de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from app.routes import auth, appointments, admin
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(appointments.router, prefix="/appointments", tags=["appointments"])
app.include_router(admin.router, prefix="/admin", tags=["admin"])

@app.get("/")
def read_root():
    return {"message": "API da Barbearia funcionando!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5173)