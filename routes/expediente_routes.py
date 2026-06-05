from flask import Blueprint

from flask_jwt_extended import (
    jwt_required
)

from models.paciente_model import (
    Paciente
)

from models.expediente_model import (
    ExpedienteClinico
)

from models.consulta_model import (
    ConsultaEncuentro
)

expediente_bp = Blueprint(
    "expediente",
    __name__
)

@expediente_bp.route(
    "/paciente/<int:id_paciente>",
    methods=["GET"]
)

@jwt_required()

def detalle_paciente(id_paciente):

    paciente =Paciente.query.get(id_paciente)

    expediente =ExpedienteClinico.query.filter_by(
        id_paciente=id_paciente
    ).first()

    consultas = []

    if expediente:

        consultas_db =ConsultaEncuentro.query.filter_by(

            id_expediente=
            expediente.id_expediente

        ).all()

        for c in consultas_db:

            consultas.append({

                "fecha":
                str(c.fecha_consulta),

                "motivo":
                c.motivo_consulta,

                "diagnostico":
                c.diagnostico_presuntivo,

                "plan":
                c.plan
            })

    return {

        "paciente":{

            "nombre":
            f"{paciente.nombre_s} "
            f"{paciente.apellido_paterno}",

            "sexo":
            paciente.sexo,

            "sangre":
            paciente.tipo_sangre,

            "telefono":
            paciente.telefono
        },

        "consultas":
        consultas
    }