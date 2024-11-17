# app/routes/item.py
from flask import Blueprint, request, jsonify
from database.init_relational_db import get_db_connection

item_blueprint = Blueprint('item', __name__)

# Crear un nuevo objeto
@item_blueprint.route('/item', methods=['POST'])
def create_item():
    data = request.json
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = """
            INSERT INTO objeto (idPersona, Nombre, Descripcion, URL_Imagen, URL_Video, ObjetoDeseado)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (data['idPersona'], data['Nombre'], data['Descripcion'], data['URL_Imagen'], data['URL_Video'], data['ObjetoDeseado']))
        connection.commit()
        return jsonify({'message': 'Objeto creado exitosamente'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

# Leer todos los objetos
@item_blueprint.route('/item', methods=['GET'])
def get_all_items():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM objeto")
        results = cursor.fetchall()
        return jsonify(results), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

# Leer un objeto por ID
@item_blueprint.route('/item/<int:idObjeto>', methods=['GET'])
def get_item_by_id(idObjeto):
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM objeto WHERE idObjeto = %s", (idObjeto,))
        result = cursor.fetchone()
        if result:
            return jsonify(result), 200
        else:
            return jsonify({'message': 'Objeto no encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

# Actualizar un objeto
@item_blueprint.route('/item/<int:idObjeto>', methods=['PUT'])
def update_item(idObjeto):
    data = request.json
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = """
            UPDATE objeto
            SET Nombre = %s, Descripcion = %s, URL_Imagen = %s, URL_Video = %s, ObjetoDeseado = %s
            WHERE idObjeto = %s
        """
        cursor.execute(query, (data['Nombre'], data['Descripcion'], data['URL_Imagen'], data['URL_Video'], data['ObjetoDeseado'], idObjeto))
        connection.commit()
        if cursor.rowcount == 0:
            return jsonify({'message': 'Objeto no encontrado'}), 404
        return jsonify({'message': 'Objeto actualizado exitosamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

# Eliminar un objeto
@item_blueprint.route('/item/<int:idObjeto>', methods=['DELETE'])
def delete_item(idObjeto):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM objeto WHERE idObjeto = %s", (idObjeto,))
        connection.commit()
        if cursor.rowcount == 0:
            return jsonify({'message': 'Objeto no encontrado'}), 404
        return jsonify({'message': 'Objeto eliminado exitosamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()
