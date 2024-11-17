# app/__init__.py
from flask import Flask
from config.config import Config
from .routes.home import home_blueprint
from .routes.api import api_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Registrar los blueprints
    app.register_blueprint(home_blueprint)
    app.register_blueprint(api_blueprint, url_prefix='/api')
    
    return app
