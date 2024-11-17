# app/routes/address.py
from flask import Blueprint, request, jsonify
from database.init_relational_db import get_db_connection

address_blueprint = Blueprint('address', __name__)

# Crear una nueva dirección para una persona
@address_blueprint.route('/address', methods=['POST'])
def create_address():
    data = request.json
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = """
            INSERT INTO direccion_Persona (idPersona, Direccion, Departamento, Provincia, Distrito)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (data['idPersona'], data['Direccion'], data['Departamento'], data['Provincia'], data['Distrito']))
        connection.commit()
        return jsonify({'message': 'Dirección creada exitosamente'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

# Leer todas las direcciones
@address_blueprint.route('/address', methods=['GET'])
def get_all_addresses():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM direccion_Persona")
        results = cursor.fetchall()
        return jsonify(results), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

# Leer dirección por ID de persona
@address_blueprint.route('/address/<int:idPersona>', methods=['GET'])
def get_address_by_person(idPersona):
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM direccion_Persona WHERE idPersona = %s", (idPersona,))
        results = cursor.fetchall()
        if results:
            return jsonify(results), 200
        else:
            return jsonify({'message': 'No se encontraron direcciones para esta persona'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

# Actualizar una dirección
@address_blueprint.route('/address/<int:idPersona>', methods=['PUT'])
def update_address(idPersona):
    data = request.json
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = """
            UPDATE direccion_Persona
            SET Direccion = %s, Departamento = %s, Provincia = %s, Distrito = %s
            WHERE idPersona = %s
        """
        cursor.execute(query, (data['Direccion'], data['Departamento'], data['Provincia'], data['Distrito'], idPersona))
        connection.commit()
        if cursor.rowcount == 0:
            return jsonify({'message': 'Persona no encontrada'}), 404
        return jsonify({'message': 'Dirección actualizada exitosamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

# Eliminar dirección por ID de persona
@address_blueprint.route('/address/<int:idPersona>', methods=['DELETE'])
def delete_address(idPersona):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM direccion_Persona WHERE idPersona = %s", (idPersona,))
        connection.commit()
        if cursor.rowcount == 0:
            return jsonify({'message': 'Dirección no encontrada para esta persona'}), 404
        return jsonify({'message': 'Dirección eliminada exitosamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()
