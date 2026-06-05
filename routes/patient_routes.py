from flask import Blueprint

from flask_jwt_extended import jwt_required

from models.patient_model import Patient

patient_bp = Blueprint(
    "patients",
    __name__
)

@patient_bp.route(
    "/patients",
    methods=["GET"]
)

@jwt_required()

def get_patients():

    patients = Patient.query.limit(100).all()

    resultado = []

    for p in patients:

        resultado.append({

            "id":p.id,

            "nombre":p.nombre,

            "apellido":p.apellido,

            "edad":p.edad,

            "presion_arterial":
            p.presion_arterial,

            "colesterol":
            p.colesterol,

            "frecuencia_cardiaca":
            p.frecuencia_cardiaca,

            "fumador":
            p.fumador
        })

    return resultado