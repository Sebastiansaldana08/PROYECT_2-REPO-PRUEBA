# app/routes/notificaciones.py
from flask import Blueprint, request, jsonify
from database.init_relational_db import get_db_connection

notificaciones_blueprint = Blueprint('notificaciones', __name__)

@notificaciones_blueprint.route('/notificaciones', methods=['GET'])
def get_notificaciones():
    """Obtener todas las notificaciones"""
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM notificaciones")
        notificaciones = cursor.fetchall()
        return jsonify(notificaciones), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

@notificaciones_blueprint.route('/notificaciones/<int:id>', methods=['GET'])
def get_notificacion_by_id(id):
    """Obtener una notificación por su ID"""
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM notificaciones WHERE idNotificacion = %s", (id,))
        notificacion = cursor.fetchone()
        if notificacion:
            return jsonify({'error': 'Notificación no encontrada'}), 404
        return jsonify(notificacion), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

@notificaciones_blueprint.route('/notificaciones', methods=['POST'])
def create_notificacion():
    """Crear una nueva notificación"""
    data = request.json
    idUsuario = data.get('idUsuario')
    Tipo = data.get('Tipo')
    Mensaje = data.get('Mensaje')
    Estado = data.get('Estado', 'No leída')  # Valor por defecto

    if not all([idUsuario, Tipo, Mensaje]):
        return jsonify({'error': 'Todos los campos requeridos deben ser enviados'}), 400

    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = """
        INSERT INTO notificaciones (idUsuario, Tipo, Mensaje, Estado)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (idUsuario, Tipo, Mensaje, Estado))
        connection.commit()
        return jsonify({'message': 'Notificación creada exitosamente'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

@notificaciones_blueprint.route('/notificaciones/<int:id>', methods=['PUT'])
def update_notificacion(id):
    """Actualizar una notificación existente"""
    data = request.json
    Estado = data.get('Estado')

    if not Estado:
        return jsonify({'error': 'El campo Estado es requerido para actualizar'}), 400

    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = """
        UPDATE notificaciones
        SET Estado = %s
        WHERE idNotificacion = %s
        """
        cursor.execute(query, (Estado, id))
        connection.commit()
        if cursor.rowcount == 0:
            return jsonify({'error': 'Notificación no encontrada'}), 404
        return jsonify({'message': 'Notificación actualizada exitosamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

@notificaciones_blueprint.route('/notificaciones/<int:id>', methods=['DELETE'])
def delete_notificacion(id):
    """Eliminar una notificación por su ID"""
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM notificaciones WHERE idNotificacion = %s", (id,))
        connection.commit()
        if cursor.rowcount == 0:
            return jsonify({'error': 'Notificación no encontrada'}), 404
        return jsonify({'message': 'Notificación eliminada exitosamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()
