from database import db

class Usuario(db.Model):

    __tablename__ = "usuario"

    id_usuario = db.Column(
        db.Integer,
        primary_key=True
    )

    id_institucion = db.Column(
        db.Integer,
        db.ForeignKey(
            "institucion.id_institucion"
        )
    )

    nombre_usuario = db.Column(
        db.String(150)
    )

    email = db.Column(
        db.String(150),
        unique=True
    )

    password_hash = db.Column(
        db.String(255)
    )

    rol = db.Column(
        db.String(50)
    )

    cedula_profesional = db.Column(
        db.String(50)
    )

    estatus = db.Column(
        db.String(50)
    )