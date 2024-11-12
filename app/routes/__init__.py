# app/routes/__init__.py
from .home import home_blueprint

def initialize_routes(app):
    # Registra las rutas (blueprints) en la aplicación Flask
    app.register_blueprint(home_blueprint)
