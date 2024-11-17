# app/routes/hobbies.py
from flask import Blueprint, request, jsonify
from database.init_relational_db import get_db_connection

hobbies_blueprint = Blueprint('hobbies', __name__)

# Crear un nuevo registro en gustos_Persona
@hobbies_blueprint.route('/hobbies', methods=['POST'])
def create_hobby():
    data = request.json
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = """
            INSERT INTO gustos_Persona (idPersona, Pasatiempos, GustosMusicales, PeliculasFavoritas)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (data['idPersona'], data['Pasatiempos'], data['GustosMusicales'], data['PeliculasFavoritas']))
        connection.commit()
        return jsonify({'message': 'Gusto creado exitosamente'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

# Leer todos los gustos
@hobbies_blueprint.route('/hobbies', methods=['GET'])
def get_all_hobbies():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM gustos_Persona")
        results = cursor.fetchall()
        return jsonify(results), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

# Leer gustos por ID de persona
@hobbies_blueprint.route('/hobbies/<int:idPersona>', methods=['GET'])
def get_hobbies_by_person(idPersona):
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM gustos_Persona WHERE idPersona = %s", (idPersona,))
        results = cursor.fetchall()
        if results:
            return jsonify(results), 200
        else:
            return jsonify({'message': 'No se encontraron gustos para esta persona'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

# Actualizar los gustos de una persona
@hobbies_blueprint.route('/hobbies/<int:idPersona>', methods=['PUT'])
def update_hobbies(idPersona):
    data = request.json
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = """
            UPDATE gustos_Persona
            SET Pasatiempos = %s, GustosMusicales = %s, PeliculasFavoritas = %s
            WHERE idPersona = %s
        """
        cursor.execute(query, (data['Pasatiempos'], data['GustosMusicales'], data['PeliculasFavoritas'], idPersona))
        connection.commit()
        if cursor.rowcount == 0:
            return jsonify({'message': 'Persona no encontrada'}), 404
        return jsonify({'message': 'Gustos actualizados exitosamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

# Eliminar gustos por ID de persona
@hobbies_blueprint.route('/hobbies/<int:idPersona>', methods=['DELETE'])
def delete_hobbies(idPersona):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM gustos_Persona WHERE idPersona = %s", (idPersona,))
        connection.commit()
        if cursor.rowcount == 0:
            return jsonify({'message': 'Gustos no encontrados para esta persona'}), 404
        return jsonify({'message': 'Gustos eliminados exitosamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()
