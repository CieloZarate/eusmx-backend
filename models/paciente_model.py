from database import db

class Paciente(db.Model):

    __tablename__ = "paciente"

    id_paciente = db.Column(
    db.Integer,
    primary_key=True,
    autoincrement=True
)

    curp = db.Column(db.String(18))

    rfc = db.Column(db.String(13))

    nombre_s = db.Column(db.String(100))

    apellido_paterno = db.Column(
        db.String(100)
    )

    apellido_materno = db.Column(
        db.String(100)
    )

    fecha_nacimiento = db.Column(
        db.Date
    )

    sexo = db.Column(
        db.String(20)
    )

    tipo_sangre = db.Column(
        db.String(5)
    )

    telefono = db.Column(
        db.String(20)
    )

    email = db.Column(
        db.String(120)
    )

    direccion = db.Column(
        db.Text
    )