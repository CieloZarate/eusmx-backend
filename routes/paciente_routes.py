from flask import Blueprint

from flask_jwt_extended import (
    jwt_required
)

from database import db

from sqlalchemy import text

paciente_bp = Blueprint(
    "paciente",
    __name__
)

@paciente_bp.route(
    "/pacientes",
    methods=["GET"]
)

@jwt_required()

def obtener_pacientes():

    query = text("""

    SELECT
    id_paciente,

    CONCAT(
        nombre_s,
        ' ',
        apellido_paterno,
        ' ',
        apellido_materno
    ) AS nombre,

    sexo,
    tipo_sangre,
    telefono,
    curp

    FROM paciente

    LIMIT 200

    """)

    result =db.session.execute(query)

    pacientes = []

    for row in result:

        pacientes.append({

            "id":
            row.id_paciente,

            "nombre":
            row.nombre,

            "sexo":
            row.sexo,

            "tipo_sangre":
            row.tipo_sangre,

            "telefono":
            row.telefono,

            "curp":
            row.curp
        })

    return pacientes

@paciente_bp.route(
    "/paciente/<int:id_paciente>",
    methods=["GET"]
)

@jwt_required()

def expediente_paciente(id_paciente):

    paciente_query = text("""

    SELECT
    p.id_paciente,

    CONCAT(
        p.nombre_s,
        ' ',
        p.apellido_paterno,
        ' ',
        p.apellido_materno
    ) AS nombre,

    p.sexo,
    p.tipo_sangre,
    p.telefono,

    ec.id_expediente

    FROM paciente p

    JOIN expediente_clinico ec
    ON p.id_paciente = ec.id_paciente

    WHERE p.id_paciente = :id

    """)

    paciente =db.session.execute(

        paciente_query,

        {

            "id":
            id_paciente
        }

    ).fetchone()

    consultas_query = text("""

    SELECT

    c.id_consulta,
    c.fecha_consulta,
    c.motivo_consulta,
    c.plan,

    d.descripcion

    FROM consulta_encuentro c

    LEFT JOIN diagnostico d
    ON c.id_consulta = d.id_consulta

    WHERE c.id_expediente = :exp

    ORDER BY c.fecha_consulta DESC

    """)

    consultas =db.session.execute(

        consultas_query,

        {

            "exp":
            paciente.id_expediente
        }

    ).fetchall()

    alergias_query = text("""

    SELECT
    sustancia_alergenica

    FROM alergia

    WHERE id_expediente = :exp

    """)

    alergias =db.session.execute(

        alergias_query,

        {

            "exp":
            paciente.id_expediente
        }

    ).fetchall()

    antecedentes_query = text("""

    SELECT
    enfermedad,
    parentesco

    FROM antecedente_familiar

    WHERE id_expediente = :exp

    """)

    antecedentes =db.session.execute(

        antecedentes_query,

        {

            "exp":
            paciente.id_expediente
        }

    ).fetchall()

    return {

        "paciente":{

            "id":
            paciente.id_paciente,

            "nombre":
            paciente.nombre,

            "sexo":
            paciente.sexo,

            "sangre":
            paciente.tipo_sangre,

            "telefono":
            paciente.telefono
        },

        "consultas":[

            {

                "id":
                c.id_consulta,

                "fecha":
                str(c.fecha_consulta),

                "motivo":
                c.motivo_consulta,

                "diagnostico":
                c.descripcion,

                "plan":
                c.plan

            }

            for c in consultas
        ],

        "alergias":[

            a.sustancia_alergenica

            for a in alergias
        ],

        "antecedentes":[

            {

                "enfermedad":
                a.enfermedad,

                "parentesco":
                a.parentesco

            }

            for a in antecedentes
        ]
    }