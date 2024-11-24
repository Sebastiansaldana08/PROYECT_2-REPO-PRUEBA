# app/__init__.py
from flask import Flask
from config.config import Config
from .routes.home import home_blueprint
from .routes.usuarios import usuarios_blueprint
from .routes.informacion_persona import informacion_persona_blueprint
from .routes.objeto import objeto_blueprint
from .routes.intercambio import intercambio_blueprint
from .routes.valoracion_intercambio import valoracion_intercambio_blueprint
from .routes.historial_propiedad import historial_propiedad_blueprint
from .routes.notificaciones import notificaciones_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Registrar los blueprints
    app.register_blueprint(home_blueprint)
    app.register_blueprint(usuarios_blueprint)
    app.register_blueprint(informacion_persona_blueprint)
    app.register_blueprint(objeto_blueprint)
    app.register_blueprint(intercambio_blueprint)
    app.register_blueprint(valoracion_intercambio_blueprint)
    app.register_blueprint(historial_propiedad_blueprint)
    app.register_blueprint(notificaciones_blueprint)
    
    return app

