# app/routes/comments.py
from flask import Blueprint, request, jsonify
from database.init_relational_db import get_db_connection

comments_blueprint = Blueprint('comments', __name__)

# Añadir un comentario a un intercambio
@comments_blueprint.route('/comments', methods=['POST'])
def add_comment():
    data = request.json
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = """
            INSERT INTO comentarios_intercambio (idIntercambio, idPersona, Comentario, Fecha)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (data['idIntercambio'], data['idPersona'], data['Comentario'], data['Fecha']))
        connection.commit()
        return jsonify({'message': 'Comentario añadido exitosamente'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

# Obtener todos los comentarios de un intercambio
@comments_blueprint.route('/comments/<int:idIntercambio>', methods=['GET'])
def get_comments_by_exchange(idIntercambio):
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        query = """
            SELECT c.idComment, c.Comentario, c.Fecha, p.Nombre AS Autor
            FROM comentarios_intercambio c
            JOIN informacion_Persona p ON c.idPersona = p.idPersona
            WHERE c.idIntercambio = %s
        """
        cursor.execute(query, (idIntercambio,))
        results = cursor.fetchall()
        if results:
            return jsonify(results), 200
        else:
            return jsonify({'message': 'No se encontraron comentarios para este intercambio'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

# Eliminar un comentario
@comments_blueprint.route('/comments/<int:idComment>', methods=['DELETE'])
def delete_comment(idComment):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM comentarios_intercambio WHERE idComment = %s", (idComment,))
        connection.commit()
        if cursor.rowcount == 0:
            return jsonify({'message': 'El comentario no se encontró'}), 404
        return jsonify({'message': 'Comentario eliminado exitosamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()
