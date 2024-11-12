# app/__init__.py
from flask import Flask
from config.config import Config
from .routes.home import home_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Registrar el blueprint de home
    app.register_blueprint(home_blueprint)
    
    return app
