# app/routes/messages.py
from flask import Blueprint, request, jsonify
from database.init_relational_db import get_db_connection

messages_blueprint = Blueprint('messages', __name__)

# Enviar un mensaje entre usuarios
@messages_blueprint.route('/messages', methods=['POST'])
def send_message():
    data = request.json
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = """
            INSERT INTO mensajes (idPersonaRemitente, idPersonaDestinatario, Mensaje, Fecha)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (data['idPersonaRemitente'], data['idPersonaDestinatario'], data['Mensaje'], data['Fecha']))
        connection.commit()
        return jsonify({'message': 'Mensaje enviado exitosamente'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

# Obtener el historial de mensajes entre dos usuarios
@messages_blueprint.route('/messages/<int:idPersona1>/<int:idPersona2>', methods=['GET'])
def get_messages_between_users(idPersona1, idPersona2):
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        query = """
            SELECT idMensaje, idPersonaRemitente, idPersonaDestinatario, Mensaje, Fecha
            FROM mensajes
            WHERE (idPersonaRemitente = %s AND idPersonaDestinatario = %s)
               OR (idPersonaRemitente = %s AND idPersonaDestinatario = %s)
            ORDER BY Fecha ASC
        """
        cursor.execute(query, (idPersona1, idPersona2, idPersona2, idPersona1))
        results = cursor.fetchall()
        if results:
            return jsonify(results), 200
        else:
            return jsonify({'message': 'No se encontraron mensajes entre estos usuarios'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

# Eliminar un mensaje
@messages_blueprint.route('/messages/<int:idMensaje>', methods=['DELETE'])
def delete_message(idMensaje):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM mensajes WHERE idMensaje = %s", (idMensaje,))
        connection.commit()
        if cursor.rowcount == 0:
            return jsonify({'message': 'Mensaje no encontrado'}), 404
        return jsonify({'message': 'Mensaje eliminado exitosamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()
