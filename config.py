import os

class Config:
    SECRET_KEY = "EUSMX_CARDIOCARE_2026_SUPER_SECRET"
    
    # Render nos dará una variable llamada DATABASE_URL
    DATABASE_URL = os.environ.get('DATABASE_URL')
    
    if DATABASE_URL:
        # Si la app corre en internet, usamos la base de datos de Render
        # Corregimos el inicio de la URL si Render la entrega como postgres://
        if DATABASE_URL.startswith("postgres://"):
            DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)
        SQLALCHEMY_DATABASE_URI = DATABASE_URL
    else:
        # Si corre en tu computadora, usa tu base de datos local
        SQLALCHEMY_DATABASE_URI = "postgresql://postgres:Cielo34@localhost:5432/cardiologia"

    SQLALCHEMY_TRACK_MODIFICATIONS = False