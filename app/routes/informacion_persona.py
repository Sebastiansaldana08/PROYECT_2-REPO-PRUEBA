# app/routes/informacion_persona.py
from flask import Blueprint, request, jsonify
from database.init_relational_db import get_db_connection

informacion_persona_blueprint = Blueprint('informacion_persona', __name__)

@informacion_persona_blueprint.route('/informacion_persona', methods=['GET'])
def get_informacion_persona():
    """Obtener toda la información de las personas"""
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM informacion_Persona")
        personas = cursor.fetchall()
        return jsonify(personas), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

@informacion_persona_blueprint.route('/informacion_persona/<int:id>', methods=['GET'])
def get_informacion_persona_by_id(id):
    """Obtener información de una persona por su ID"""
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM informacion_Persona WHERE idPersona = %s", (id,))
        persona = cursor.fetchone()
        if persona:
            return jsonify(persona), 200
        else:
            return jsonify({'error': 'Persona no encontrada'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

@informacion_persona_blueprint.route('/informacion_persona', methods=['POST'])
def create_informacion_persona():
    """Crear información de una nueva persona"""
    data = request.json
    DNI = data.get('DNI')
    Nombre = data.get('Nombre')
    FechaNacimiento = data.get('FechaNacimiento')
    DireccionCorreo = data.get('DireccionCorreo')
    PuntuacionPromedio = data.get('PuntuacionPromedio', None)
    
    if not all([DNI, Nombre, FechaNacimiento, DireccionCorreo]):
        return jsonify({'error': 'Todos los campos requeridos deben ser enviados'}), 400
    
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = """
        INSERT INTO informacion_Persona (DNI, Nombre, FechaNacimiento, DireccionCorreo, PuntuacionPromedio)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (DNI, Nombre, FechaNacimiento, DireccionCorreo, PuntuacionPromedio))
        connection.commit()
        return jsonify({'message': 'Persona creada exitosamente'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

@informacion_persona_blueprint.route('/informacion_persona/<int:id>', methods=['PUT'])
def update_informacion_persona(id):
    """Actualizar información de una persona existente"""
    data = request.json
    DNI = data.get('DNI')
    Nombre = data.get('Nombre')
    FechaNacimiento = data.get('FechaNacimiento')
    DireccionCorreo = data.get('DireccionCorreo')
    PuntuacionPromedio = data.get('PuntuacionPromedio')
    
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = """
        UPDATE informacion_Persona
        SET DNI = %s, Nombre = %s, FechaNacimiento = %s, DireccionCorreo = %s, PuntuacionPromedio = %s
        WHERE idPersona = %s
        """
        cursor.execute(query, (DNI, Nombre, FechaNacimiento, DireccionCorreo, PuntuacionPromedio, id))
        connection.commit()
        if cursor.rowcount == 0:
            return jsonify({'error': 'Persona no encontrada'}), 404
        return jsonify({'message': 'Persona actualizada exitosamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

@informacion_persona_blueprint.route('/informacion_persona/<int:id>', methods=['DELETE'])
def delete_informacion_persona(id):
    """Eliminar información de una persona por su ID"""
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM informacion_Persona WHERE idPersona = %s", (id,))
        connection.commit()
        if cursor.rowcount == 0:
            return jsonify({'error': 'Persona no encontrada'}), 404
        return jsonify({'message': 'Persona eliminada exitosamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()
