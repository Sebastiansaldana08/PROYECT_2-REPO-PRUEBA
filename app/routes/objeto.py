# app/routes/objeto.py
from flask import Blueprint, request, jsonify
from database.init_relational_db import get_db_connection

objeto_blueprint = Blueprint('objeto', __name__)

@objeto_blueprint.route('/objetos', methods=['GET'])
def get_objetos():
    """Obtener todos los objetos"""
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM objeto")
        objetos = cursor.fetchall()
        return jsonify(objetos), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

@objeto_blueprint.route('/objetos/<int:id>', methods=['GET'])
def get_objeto_by_id(id):
    """Obtener un objeto por su ID"""
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM objeto WHERE idObjeto = %s", (id,))
        objeto = cursor.fetchone()
        if objeto:
            return jsonify(objeto), 200
        else:
            return jsonify({'error': 'Objeto no encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

@objeto_blueprint.route('/objetos', methods=['POST'])
def create_objeto():
    """Crear un nuevo objeto"""
    data = request.json
    idPersona = data.get('idPersona')
    Nombre = data.get('Nombre')
    Descripcion = data.get('Descripcion')
    URL_Imagen = data.get('URL_Imagen')
    URL_Video = data.get('URL_Video')
    ObjetoDeseado = data.get('ObjetoDeseado')
    Estado = data.get('Estado', 'Disponible')  # Estado por defecto: Disponible
    
    if not all([idPersona, Nombre, Descripcion, URL_Imagen, URL_Video, ObjetoDeseado]):
        return jsonify({'error': 'Todos los campos requeridos deben ser enviados'}), 400
    
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = """
        INSERT INTO objeto (idPersona, Nombre, Descripcion, URL_Imagen, URL_Video, ObjetoDeseado, Estado)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (idPersona, Nombre, Descripcion, URL_Imagen, URL_Video, ObjetoDeseado, Estado))
        connection.commit()
        return jsonify({'message': 'Objeto creado exitosamente'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

@objeto_blueprint.route('/objetos/<int:id>', methods=['PUT'])
def update_objeto(id):
    """Actualizar un objeto existente"""
    data = request.json
    Nombre = data.get('Nombre')
    Descripcion = data.get('Descripcion')
    URL_Imagen = data.get('URL_Imagen')
    URL_Video = data.get('URL_Video')
    ObjetoDeseado = data.get('ObjetoDeseado')
    Estado = data.get('Estado')
    
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = """
        UPDATE objeto
        SET Nombre = %s, Descripcion = %s, URL_Imagen = %s, URL_Video = %s, ObjetoDeseado = %s, Estado = %s
        WHERE idObjeto = %s
        """
        cursor.execute(query, (Nombre, Descripcion, URL_Imagen, URL_Video, ObjetoDeseado, Estado, id))
        connection.commit()
        if cursor.rowcount == 0:
            return jsonify({'error': 'Objeto no encontrado'}), 404
        return jsonify({'message': 'Objeto actualizado exitosamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

@objeto_blueprint.route('/objetos/<int:id>', methods=['DELETE'])
def delete_objeto(id):
    """Eliminar un objeto por su ID"""
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM objeto WHERE idObjeto = %s", (id,))
        connection.commit()
        if cursor.rowcount == 0:
            return jsonify({'error': 'Objeto no encontrado'}), 404
        return jsonify({'message': 'Objeto eliminado exitosamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()
