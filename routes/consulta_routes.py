from flask import Blueprint, request

from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)

from database import db

from sqlalchemy import text

from datetime import datetime

consulta_bp = Blueprint(
    "consulta",
    __name__
)

@consulta_bp.route(
    "/nueva-consulta",
    methods=["POST"]
)
@jwt_required()
def nueva_consulta():

    data = request.json

    id_paciente = data["id_paciente"]

    motivo = data["motivo"]

    diagnostico = data["diagnostico"]

    plan = data["plan"]

    expediente_query = text("""

    SELECT id_expediente

    FROM expediente_clinico

    WHERE id_paciente = :id

    LIMIT 1

    """)

    expediente = db.session.execute(

        expediente_query,

        {
            "id": id_paciente
        }

    ).fetchone()

    id_expediente = expediente.id_expediente

    id_medico = get_jwt_identity()

    insert_consulta = text("""

    INSERT INTO consulta_encuentro (

        id_expediente,
        id_usuario_medico,
        fecha_consulta,
        motivo_consulta,
        plan

    )

    VALUES (

        :exp,
        :med,
        :fecha,
        :motivo,
        :plan
    )

    RETURNING id_consulta

    """)

    consulta = db.session.execute(

        insert_consulta,

        {

            "exp": id_expediente,

            "med": id_medico,

            "fecha": datetime.now(),

            "motivo": motivo,

            "plan": plan
        }

    ).fetchone()

    id_consulta = consulta.id_consulta

    insert_diag = text("""

    INSERT INTO diagnostico (

        id_consulta,
        id_expediente,
        descripcion,
        fecha_diagnostico,
        tipo,
        estatus

    )

    VALUES (

        :consulta,
        :exp,
        :diag,
        :fecha,
        'Principal',
        'Activo'
    )

    """)

    db.session.execute(

        insert_diag,

        {

            "consulta": id_consulta,

            "exp": id_expediente,

            "diag": diagnostico,

            "fecha": datetime.now()
        }

    )

    db.session.commit()

    return {

        "mensaje":
        "Consulta guardada correctamente"
    }


@consulta_bp.route(
    "/eliminar-consulta/<int:id>",
    methods=["DELETE"]
)
@jwt_required()
def eliminar_consulta(id):

    query = text("""

    DELETE FROM consulta_encuentro

    WHERE id_consulta = :id

    """)

    db.session.execute(

        query,

        {
            "id": id
        }
    )

    db.session.commit()

    return {
        "mensaje":
        "Consulta eliminada"
    }


@consulta_bp.route(
    "/editar-consulta/<int:id>",
    methods=["PUT"]
)
@jwt_required()
def editar_consulta(id):

    data = request.json

    update_consulta = text("""

    UPDATE consulta_encuentro

    SET

        motivo_consulta = :motivo,
        plan = :plan

    WHERE id_consulta = :id

    """)

    db.session.execute(

        update_consulta,

        {

            "motivo":
            data["motivo"],

            "plan":
            data["plan"],

            "id":
            id
        }
    )

    update_diag = text("""

    UPDATE diagnostico

    SET descripcion = :diag

    WHERE id_consulta = :id

    """)

    db.session.execute(

        update_diag,

        {

            "diag":
            data["diagnostico"],

            "id":
            id
        }
    )

    db.session.commit()

    return {
        "mensaje":
        "Consulta actualizada"
    }