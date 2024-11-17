# app/routes/history.py
from flask import Blueprint, request, jsonify
from database.init_relational_db import get_db_connection

history_blueprint = Blueprint('history', __name__)

# Registrar un nuevo historial de propiedad
@history_blueprint.route('/history', methods=['POST'])
def create_history():
    data = request.json
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = """
            INSERT INTO historial_Propiedad (idPersona, idObjeto, FechaAdquisicion, FechaCambio)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (data['idPersona'], data['idObjeto'], data['FechaAdquisicion'], data.get('FechaCambio')))
        connection.commit()
        return jsonify({'message': 'Historial registrado exitosamente'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

# Leer todo el historial de propiedad
@history_blueprint.route('/history', methods=['GET'])
def get_all_histories():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM historial_Propiedad")
        results = cursor.fetchall()
        return jsonify(results), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

# Leer historial por ID de objeto
@history_blueprint.route('/history/<int:idObjeto>', methods=['GET'])
def get_history_by_object(idObjeto):
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM historial_Propiedad WHERE idObjeto = %s ORDER BY FechaAdquisicion ASC", (idObjeto,))
        results = cursor.fetchall()
        if results:
            return jsonify(results), 200
        else:
            return jsonify({'message': 'No se encontró historial para este objeto'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

# Actualizar un registro de historial
@history_blueprint.route('/history/<int:idHistorial>', methods=['PUT'])
def update_history(idHistorial):
    data = request.json
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = """
            UPDATE historial_Propiedad
            SET idPersona = %s, idObjeto = %s, FechaAdquisicion = %s, FechaCambio = %s
            WHERE idHistorial = %s
        """
        cursor.execute(query, (data['idPersona'], data['idObjeto'], data['FechaAdquisicion'], data.get('FechaCambio'), idHistorial))
        connection.commit()
        if cursor.rowcount == 0:
            return jsonify({'message': 'Registro de historial no encontrado'}), 404
        return jsonify({'message': 'Historial actualizado exitosamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

# Eliminar un registro de historial
@history_blueprint.route('/history/<int:idHistorial>', methods=['DELETE'])
def delete_history(idHistorial):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM historial_Propiedad WHERE idHistorial = %s", (idHistorial,))
        connection.commit()
        if cursor.rowcount == 0:
            return jsonify({'message': 'Registro de historial no encontrado'}), 404
        return jsonify({'message': 'Historial eliminado exitosamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()
