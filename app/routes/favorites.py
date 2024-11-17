# app/routes/favorites.py
from flask import Blueprint, request, jsonify
from database.init_relational_db import get_db_connection

favorites_blueprint = Blueprint('favorites', __name__)

# Añadir un objeto a favoritos
@favorites_blueprint.route('/favorites', methods=['POST'])
def add_favorite():
    data = request.json
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = """
            INSERT INTO favoritos (idPersona, idObjetoFavorito)
            VALUES (%s, %s)
        """
        cursor.execute(query, (data['idPersona'], data['idObjetoFavorito']))
        connection.commit()
        return jsonify({'message': 'Objeto añadido a favoritos exitosamente'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

# Obtener todos los favoritos de un usuario
@favorites_blueprint.route('/favorites/<int:idPersona>', methods=['GET'])
def get_favorites_by_person(idPersona):
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        query = """
            SELECT f.idFavorite, f.idObjetoFavorito, o.Nombre, o.Descripcion
            FROM favoritos f
            JOIN objeto o ON f.idObjetoFavorito = o.idObjeto
            WHERE f.idPersona = %s
        """
        cursor.execute(query, (idPersona,))
        results = cursor.fetchall()
        if results:
            return jsonify(results), 200
        else:
            return jsonify({'message': 'No se encontraron favoritos para este usuario'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

# Eliminar un favorito
@favorites_blueprint.route('/favorites/<int:idFavorite>', methods=['DELETE'])
def delete_favorite(idFavorite):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM favoritos WHERE idFavorite = %s", (idFavorite,))
        connection.commit()
        if cursor.rowcount == 0:
            return jsonify({'message': 'El favorito no se encontró'}), 404
        return jsonify({'message': 'Favorito eliminado exitosamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()
