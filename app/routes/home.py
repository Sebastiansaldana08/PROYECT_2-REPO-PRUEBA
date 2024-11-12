# app/routes/home.py
from flask import Blueprint, render_template
from database.init_relational_db import get_db_connection
import mysql.connector

home_blueprint = Blueprint('home', __name__)

@home_blueprint.route('/')
def index():
    connection = None
    host = None
    user = None
    
    # Intentar conectar a la base de datos
    try:
        connection = get_db_connection()
        if connection.is_connected():
            # Obtener información de conexión para mostrar en la plantilla
            host = connection.server_host
            user = connection.user
            message = "¡Conexión exitosa a la base de datos!"
        else:
            message = "No se pudo conectar a la base de datos."
    except mysql.connector.Error as err:
        message = f"Error al conectar: {err}"
    finally:
        if connection and connection.is_connected():
            connection.close()
    
    return render_template('index.html', message=message, host=host, user=user)
