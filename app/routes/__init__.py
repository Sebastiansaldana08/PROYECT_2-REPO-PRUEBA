from .home import home_blueprint
from .usuarios import usuarios_blueprint
from .informacion_persona import informacion_persona_blueprint
from .objeto import objeto_blueprint
from .intercambio import intercambio_blueprint
from .valoracion_intercambio import valoracion_intercambio_blueprint
from .historial_propiedad import historial_propiedad_blueprint
from .notificaciones import notificaciones_blueprint
from .neo4j_routes import neo4j_blueprint

def initialize_routes(app):
    app.register_blueprint(home_blueprint)
    app.register_blueprint(usuarios_blueprint)
    app.register_blueprint(informacion_persona_blueprint)
    app.register_blueprint(objeto_blueprint)
    app.register_blueprint(intercambio_blueprint)
    app.register_blueprint(valoracion_intercambio_blueprint)
    app.register_blueprint(historial_propiedad_blueprint)
    app.register_blueprint(notificaciones_blueprint)
    app.register_blueprint(neo4j_blueprint)