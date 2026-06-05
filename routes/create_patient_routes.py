from flask import Blueprint, request

from flask_jwt_extended import jwt_required

from database import db

from models.paciente_model import Paciente
from models.expediente_model import ExpedienteClinico

from datetime import datetime

create_patient_bp = Blueprint(
    "create_patient",
    __name__
)

@create_patient_bp.route(
    "/crear-paciente",
    methods=["POST"]
)
@jwt_required()
def crear_paciente():

    try:

        data = request.json

        print("DATOS RECIBIDOS:")
        print(data)

        paciente = Paciente(

            nombre_s=data["nombre"],

            apellido_paterno=data["apellido_p"],

            apellido_materno=data["apellido_m"],

            curp=data["curp"],

            sexo=data["sexo"],

            tipo_sangre=data["sangre"],

            telefono=data["telefono"],

            email=data["email"],

            direccion=data["direccion"],

            fecha_nacimiento=data["fecha_nacimiento"]

        )

        db.session.add(paciente)

        db.session.commit()

        expediente = ExpedienteClinico(

            id_paciente=paciente.id_paciente,

            fecha_apertura=datetime.now(),

            estatus="Activo",

            tipo_expediente="Cardiológico",

            observaciones_generales=
            "Expediente creado automáticamente"

        )

        db.session.add(expediente)

        db.session.commit()

        return {

            "mensaje":
            "Paciente creado correctamente",

            "id_paciente":
            paciente.id_paciente

        }, 200

    except Exception as e:

        print("=================================")
        print("ERROR AL CREAR PACIENTE")
        print(str(e))
        print("=================================")

        return {

            "error": str(e)

        }, 500
        