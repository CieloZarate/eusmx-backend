from database import db

from datetime import datetime

class Consultation(db.Model):

    __tablename__ = "consultations"

    id = db.Column(db.Integer, primary_key=True)

    paciente_id = db.Column(
        db.Integer,
        db.ForeignKey("patients.id")
    )

    medico_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )

    diagnostico = db.Column(db.Text)

    tratamiento = db.Column(db.Text)

    observaciones = db.Column(db.Text)

    fecha = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )