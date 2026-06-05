from database import db

class ExpedienteClinico(db.Model):

    __tablename__ = "expediente_clinico"

    id_expediente = db.Column(
    db.Integer,
    primary_key=True,
    autoincrement=True
)

    id_paciente = db.Column(
        db.Integer
    )

    fecha_apertura = db.Column(
        db.DateTime
    )

    estatus = db.Column(
        db.String(50)
    )

    tipo_expediente = db.Column(
        db.String(50)
    )

    observaciones_generales = db.Column(db.Text)