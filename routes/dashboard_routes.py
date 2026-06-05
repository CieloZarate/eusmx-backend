from flask import Blueprint
from flask_jwt_extended import jwt_required

dashboard_bp = Blueprint(
    "dashboard",
    __name__
)

@dashboard_bp.route(
    "/dashboard",
    methods=["GET"]
)
@jwt_required()
def dashboard():

    return {

        "pacientes": 248,

        "medicos": 12,

        "consultas_hoy": 87,

        "riesgo_alto": 14,

        "seguimiento": 63,

        "prioritarios":[

            {
                "nombre":"Juan Pérez",
                "riesgo":"ALTO",
                "detalle":"Arritmia cardiaca"
            },

            {
                "nombre":"María López",
                "riesgo":"ALTO",
                "detalle":"Hipertensión severa"
            },

            {
                "nombre":"Carlos Martínez",
                "riesgo":"MEDIO",
                "detalle":"Seguimiento postoperatorio"
            },

            {
                "nombre":"Laura Hernández",
                "riesgo":"ALTO",
                "detalle":"Insuficiencia cardiaca"
            }

        ],

        "grafica":{

            "labels":[
                "Lun",
                "Mar",
                "Mié",
                "Jue",
                "Vie",
                "Sáb",
                "Dom"
            ],

            "data":[
                35,
                42,
                39,
                51,
                47,
                58,
                63
            ]
        }
    }