# app/routes/person.py
from flask import Blueprint, request, jsonify
from database.init_relational_db import get_db_connection

person_blueprint = Blueprint('person', __name__)

# Crear un nuevo registro en informacion_Persona
@person_blueprint.route('/person', methods=['POST'])
def create_person():
    data = request.json
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = """
            INSERT INTO informacion_Persona (DNI, Nombre, FechaNacimiento, DireccionCorreo, PuntuacionPromedio)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (data['DNI'], data['Nombre'], data['FechaNacimiento'], data['DireccionCorreo'], data.get('PuntuacionPromedio')))
        connection.commit()
        return jsonify({'message': 'Persona creada exitosamente'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

# Leer todas las personas
@person_blueprint.route('/person', methods=['GET'])
def get_all_persons():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM informacion_Persona")
        results = cursor.fetchall()
        return jsonify(results), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

# Leer una persona por ID
@person_blueprint.route('/person/<int:id>', methods=['GET'])
def get_person_by_id(id):
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM informacion_Persona WHERE idPersona = %s", (id,))
        result = cursor.fetchone()
        if result:
            return jsonify(result), 200
        else:
            return jsonify({'message': 'Persona no encontrada'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

# Actualizar una persona
@person_blueprint.route('/person/<int:id>', methods=['PUT'])
def update_person(id):
    data = request.json
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = """
            UPDATE informacion_Persona
            SET DNI = %s, Nombre = %s, FechaNacimiento = %s, DireccionCorreo = %s, PuntuacionPromedio = %s
            WHERE idPersona = %s
        """
        cursor.execute(query, (data['DNI'], data['Nombre'], data['FechaNacimiento'], data['DireccionCorreo'], data.get('PuntuacionPromedio'), id))
        connection.commit()
        if cursor.rowcount == 0:
            return jsonify({'message': 'Persona no encontrada'}), 404
        return jsonify({'message': 'Persona actualizada exitosamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

# Eliminar una persona
@person_blueprint.route('/person/<int:id>', methods=['DELETE'])
def delete_person(id):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM informacion_Persona WHERE idPersona = %s", (id,))
        connection.commit()
        if cursor.rowcount == 0:
            return jsonify({'message': 'Persona no encontrada'}), 404
        return jsonify({'message': 'Persona eliminada exitosamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()
