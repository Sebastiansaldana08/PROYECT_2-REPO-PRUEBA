# app/routes/rating.py
from flask import Blueprint, request, jsonify
from database.init_relational_db import get_db_connection

rating_blueprint = Blueprint('rating', __name__)

# Crear una nueva valoración
@rating_blueprint.route('/rating', methods=['POST'])
def create_rating():
    data = request.json
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = """
            INSERT INTO valoracion_Intercambio (idIntercambio, idPersona1, Puntuacion, Comentario, idPersona2, Fecha)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (data['idIntercambio'], data['idPersona1'], data['Puntuacion'], data.get('Comentario'), data['idPersona2'], data['Fecha']))
        connection.commit()
        return jsonify({'message': 'Valoración registrada exitosamente'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

# Leer todas las valoraciones
@rating_blueprint.route('/rating', methods=['GET'])
def get_all_ratings():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM valoracion_Intercambio")
        results = cursor.fetchall()
        return jsonify(results), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

# Leer una valoración por ID de intercambio
@rating_blueprint.route('/rating/<int:idIntercambio>', methods=['GET'])
def get_rating_by_exchange(idIntercambio):
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM valoracion_Intercambio WHERE idIntercambio = %s", (idIntercambio,))
        results = cursor.fetchall()
        if results:
            return jsonify(results), 200
        else:
            return jsonify({'message': 'No se encontraron valoraciones para este intercambio'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

# Actualizar una valoración
@rating_blueprint.route('/rating/<int:idValoracion>', methods=['PUT'])
def update_rating(idValoracion):
    data = request.json
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = """
            UPDATE valoracion_Intercambio
            SET Puntuacion = %s, Comentario = %s
            WHERE idValoracion = %s
        """
        cursor.execute(query, (data['Puntuacion'], data.get('Comentario'), idValoracion))
        connection.commit()
        if cursor.rowcount == 0:
            return jsonify({'message': 'Valoración no encontrada'}), 404
        return jsonify({'message': 'Valoración actualizada exitosamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

# Eliminar una valoración
@rating_blueprint.route('/rating/<int:idValoracion>', methods=['DELETE'])
def delete_rating(idValoracion):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM valoracion_Intercambio WHERE idValoracion = %s", (idValoracion,))
        connection.commit()
        if cursor.rowcount == 0:
            return jsonify({'message': 'Valoración no encontrada'}), 404
        return jsonify({'message': 'Valoración eliminada exitosamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()
