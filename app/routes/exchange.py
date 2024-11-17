# app/routes/exchange.py
from flask import Blueprint, request, jsonify
from database.init_relational_db import get_db_connection

exchange_blueprint = Blueprint('exchange', __name__)

# Crear un nuevo intercambio
@exchange_blueprint.route('/exchange', methods=['POST'])
def create_exchange():
    data = request.json
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = """
            INSERT INTO Intercambio (idPersona1, idObjeto1, idPersona2, idObjeto2, Fecha)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (data['idPersona1'], data['idObjeto1'], data['idPersona2'], data['idObjeto2'], data['Fecha']))
        connection.commit()
        return jsonify({'message': 'Intercambio registrado exitosamente'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

# Leer todos los intercambios
@exchange_blueprint.route('/exchange', methods=['GET'])
def get_all_exchanges():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Intercambio")
        results = cursor.fetchall()
        return jsonify(results), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

# Leer un intercambio por ID
@exchange_blueprint.route('/exchange/<int:idIntercambio>', methods=['GET'])
def get_exchange_by_id(idIntercambio):
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Intercambio WHERE idIntercambio = %s", (idIntercambio,))
        result = cursor.fetchone()
        if result:
            return jsonify(result), 200
        else:
            return jsonify({'message': 'Intercambio no encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

# Actualizar un intercambio
@exchange_blueprint.route('/exchange/<int:idIntercambio>', methods=['PUT'])
def update_exchange(idIntercambio):
    data = request.json
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = """
            UPDATE Intercambio
            SET idPersona1 = %s, idObjeto1 = %s, idPersona2 = %s, idObjeto2 = %s, Fecha = %s
            WHERE idIntercambio = %s
        """
        cursor.execute(query, (data['idPersona1'], data['idObjeto1'], data['idPersona2'], data['idObjeto2'], data['Fecha'], idIntercambio))
        connection.commit()
        if cursor.rowcount == 0:
            return jsonify({'message': 'Intercambio no encontrado'}), 404
        return jsonify({'message': 'Intercambio actualizado exitosamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

# Eliminar un intercambio
@exchange_blueprint.route('/exchange/<int:idIntercambio>', methods=['DELETE'])
def delete_exchange(idIntercambio):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM Intercambio WHERE idIntercambio = %s", (idIntercambio,))
        connection.commit()
        if cursor.rowcount == 0:
            return jsonify({'message': 'Intercambio no encontrado'}), 404
        return jsonify({'message': 'Intercambio eliminado exitosamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()
