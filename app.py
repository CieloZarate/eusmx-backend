from flask import Flask

from flask_cors import CORS

from flask_jwt_extended import JWTManager

from config import Config

from database import db

# IMPORTAR RUTAS
from routes.auth_routes import auth_bp
from routes.paciente_routes import paciente_bp
from routes.dashboard_routes import dashboard_bp
from routes.expediente_routes import expediente_bp
from routes.create_patient_routes import create_patient_bp
from routes.consulta_routes import consulta_bp

app = Flask(__name__)

app.config.from_object(Config)

CORS(app)

jwt = JWTManager(app)

db.init_app(app)

# IMPORTAR MODELOS
from models.usuario_model import Usuario

# REGISTRAR RUTAS
app.register_blueprint(auth_bp)
app.register_blueprint(paciente_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(expediente_bp)
app.register_blueprint(create_patient_bp)
app.register_blueprint(consulta_bp)

@app.route("/")

def home():

    return {
        "mensaje":"EUS-MX CardioCare funcionando"
    }

if __name__ == "__main__":

    app.run(debug=True)