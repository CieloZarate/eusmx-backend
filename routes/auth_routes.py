from flask import Blueprint, request

from flask_jwt_extended import (
    create_access_token
)

from models.usuario_model import Usuario

auth_bp = Blueprint(
    "auth",
    __name__
)

@auth_bp.route(
    "/login",
    methods=["POST"]
)

def login():

    data = request.json

    usuario = Usuario.query.filter_by(

        cedula_profesional =
        data["cedula"]

    ).first()

    if not usuario:

        return {

            "mensaje":
            "Usuario no encontrado"

        },404

    if usuario.password_hash == data["password"]:

        token = create_access_token(

            identity =
            str(usuario.id_usuario)

        )

        return {

            "token":token,

            "nombre":
            usuario.nombre_usuario,

            "rol":
            usuario.rol

        }

    return {

        "mensaje":
        "Contraseña incorrecta"

    },401