from database import db

class Patient(db.Model):

    __tablename__ = "patients"

    id = db.Column(db.Integer, primary_key=True)

    nombre = db.Column(db.String(100))

    apellido = db.Column(db.String(100))

    edad = db.Column(db.Integer)

    sexo = db.Column(db.String(20))

    curp = db.Column(db.String(18))

    nss = db.Column(db.String(20))

    telefono = db.Column(db.String(20))

    direccion = db.Column(db.String(200))

    diabetes = db.Column(db.Boolean)

    hipertension = db.Column(db.Boolean)

    peso = db.Column(db.Float)

    altura = db.Column(db.Float)

    presion_arterial = db.Column(
        db.String(20)
    )

    colesterol = db.Column(
        db.Float
    )

    frecuencia_cardiaca = db.Column(
        db.Integer
    )

    fumador = db.Column(
        db.Boolean
    )

    antecedentes_cardiacos = db.Column(
        db.Boolean
    )

    imc = db.Column(
        db.Float
    )

    medico_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )