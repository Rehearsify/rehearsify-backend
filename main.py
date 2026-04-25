from fastapi import FastAPI
from sqlmodel import SQLModel, create_engine, Session
import os

# Configuracion de la DB desde variables de entorno
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

app = FastAPI(title="Rehearsify API")

@app.on_event("startup")
def on_startup():
  # Crea las tablas de la DB si no existen (Se implementará Alembic)
  SQLModel.metadata.create_all(engine)

@app.get("/")
def read_root():
  return {"status": "online", "project": "Rehearsify"}

@app.get("/health")
def health_check():
  return {"database": "connected"}