# app/routes/valoracion_intercambio.py
from flask import Blueprint, request, jsonify
from database.init_relational_db import get_db_connection

valoracion_intercambio_blueprint = Blueprint('valoracion_intercambio', __name__)

@valoracion_intercambio_blueprint.route('/valoraciones', methods=['GET'])
def get_valoraciones():
    """Obtener todas las valoraciones"""
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM valoracion_Intercambio")
        valoraciones = cursor.fetchall()
        return jsonify(valoraciones), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

@valoracion_intercambio_blueprint.route('/valoraciones/<int:id>', methods=['GET'])
def get_valoracion_by_id(id):
    """Obtener una valoración por su ID"""
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM valoracion_Intercambio WHERE idValoracion = %s", (id,))
        valoracion = cursor.fetchone()
        if valoracion:
            return jsonify(valoracion), 200
        else:
            return jsonify({'error': 'Valoración no encontrada'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

@valoracion_intercambio_blueprint.route('/valoraciones', methods=['POST'])
def create_valoracion():
    """Crear una nueva valoración"""
    data = request.json
    idIntercambio = data.get('idIntercambio')
    idPersona1 = data.get('idPersona1')
    Puntuacion = data.get('Puntuacion')
    Comentario = data.get('Comentario', None)
    idPersona2 = data.get('idPersona2')
    
    if not all([idIntercambio, idPersona1, Puntuacion, idPersona2]):
        return jsonify({'error': 'Todos los campos requeridos deben ser enviados'}), 400
    
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = """
        INSERT INTO valoracion_Intercambio (idIntercambio, idPersona1, Puntuacion, Comentario, idPersona2)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (idIntercambio, idPersona1, Puntuacion, Comentario, idPersona2))
        connection.commit()
        return jsonify({'message': 'Valoración creada exitosamente'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

@valoracion_intercambio_blueprint.route('/valoraciones/<int:id>', methods=['PUT'])
def update_valoracion(id):
    """Actualizar una valoración existente"""
    data = request.json
    Puntuacion = data.get('Puntuacion')
    Comentario = data.get('Comentario', None)
    
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = """
        UPDATE valoracion_Intercambio
        SET Puntuacion = %s, Comentario = %s
        WHERE idValoracion = %s
        """
        cursor.execute(query, (Puntuacion, Comentario, id))
        connection.commit()
        if cursor.rowcount == 0:
            return jsonify({'error': 'Valoración no encontrada'}), 404
        return jsonify({'message': 'Valoración actualizada exitosamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

@valoracion_intercambio_blueprint.route('/valoraciones/<int:id>', methods=['DELETE'])
def delete_valoracion(id):
    """Eliminar una valoración por su ID"""
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM valoracion_Intercambio WHERE idValoracion = %s", (id,))
        connection.commit()
        if cursor.rowcount == 0:
            return jsonify({'error': 'Valoración no encontrada'}), 404
        return jsonify({'message': 'Valoración eliminada exitosamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()
