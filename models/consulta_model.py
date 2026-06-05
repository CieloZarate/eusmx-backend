from database import db

class ConsultaEncuentro(db.Model):

    __tablename__ = "consulta_encuentro"

    id_consulta = db.Column(
        db.Integer,
        primary_key=True
    )

    id_expediente = db.Column(
        db.Integer
    )

    fecha_consulta = db.Column(
        db.DateTime
    )

    motivo_consulta =db.Column(db.Text)

    subjetivo =db.Column(db.Text)

    objetivo =db.Column(db.Text)

    plan =db.Column(db.Text)

    diagnostico_presuntivo =db.Column(db.Text)