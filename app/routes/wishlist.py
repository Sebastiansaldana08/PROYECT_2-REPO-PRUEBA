# app/routes/wishlist.py
from flask import Blueprint, request, jsonify
from database.init_relational_db import get_db_connection

wishlist_blueprint = Blueprint('wishlist', __name__)

# Crear un nuevo deseo
@wishlist_blueprint.route('/wishlist', methods=['POST'])
def create_wishlist_item():
    data = request.json
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = """
            INSERT INTO lista_deseos (idPersona, idObjetoDeseado)
            VALUES (%s, %s)
        """
        cursor.execute(query, (data['idPersona'], data['idObjetoDeseado']))
        connection.commit()
        return jsonify({'message': 'Objeto añadido a la lista de deseos exitosamente'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

# Leer todos los deseos de un usuario
@wishlist_blueprint.route('/wishlist/<int:idPersona>', methods=['GET'])
def get_wishlist_by_person(idPersona):
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        query = """
            SELECT l.idWishlist, l.idObjetoDeseado, o.Nombre, o.Descripcion
            FROM lista_deseos l
            JOIN objeto o ON l.idObjetoDeseado = o.idObjeto
            WHERE l.idPersona = %s
        """
        cursor.execute(query, (idPersona,))
        results = cursor.fetchall()
        if results:
            return jsonify(results), 200
        else:
            return jsonify({'message': 'No se encontraron deseos para este usuario'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

# Eliminar un deseo de la lista
@wishlist_blueprint.route('/wishlist/<int:idWishlist>', methods=['DELETE'])
def delete_wishlist_item(idWishlist):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM lista_deseos WHERE idWishlist = %s", (idWishlist,))
        connection.commit()
        if cursor.rowcount == 0:
            return jsonify({'message': 'El deseo no se encontró en la lista'}), 404
        return jsonify({'message': 'Deseo eliminado exitosamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()
