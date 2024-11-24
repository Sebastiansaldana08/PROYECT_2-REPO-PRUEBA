# app/routes/usuarios.py
from flask import Blueprint, request, jsonify
from database.init_relational_db import get_db_connection

usuarios_blueprint = Blueprint('usuarios', __name__)

@usuarios_blueprint.route('/usuarios', methods=['GET'])
def get_usuarios():
    """Obtener todos los usuarios"""
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios")
        usuarios = cursor.fetchall()
        return jsonify(usuarios), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

@usuarios_blueprint.route('/usuarios/<int:id>', methods=['GET'])
def get_usuario_by_id(id):
    """Obtener un usuario por su ID"""
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios WHERE idUsuario = %s", (id,))
        usuario = cursor.fetchone()
        if usuario:
            return jsonify(usuario), 200
        else:
            return jsonify({'error': 'Usuario no encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

@usuarios_blueprint.route('/usuarios', methods=['POST'])
def create_usuario():
    """Crear un nuevo usuario"""
    data = request.json
    username = data.get('username')
    password = data.get('password')
    idPersona = data.get('idPersona')
    
    if not username or not password:
        return jsonify({'error': 'Username y Password son requeridos'}), 400
    
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = "INSERT INTO usuarios (username, password, idPersona) VALUES (%s, %s, %s)"
        cursor.execute(query, (username, password, idPersona))
        connection.commit()
        return jsonify({'message': 'Usuario creado exitosamente'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

@usuarios_blueprint.route('/usuarios/<int:id>', methods=['PUT'])
def update_usuario(id):
    """Actualizar un usuario existente"""
    data = request.json
    username = data.get('username')
    password = data.get('password')
    idPersona = data.get('idPersona')
    
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = """
        UPDATE usuarios
        SET username = %s, password = %s, idPersona = %s
        WHERE idUsuario = %s
        """
        cursor.execute(query, (username, password, idPersona, id))
        connection.commit()
        if cursor.rowcount == 0:
            return jsonify({'error': 'Usuario no encontrado'}), 404
        return jsonify({'message': 'Usuario actualizado exitosamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

@usuarios_blueprint.route('/usuarios/<int:id>', methods=['DELETE'])
def delete_usuario(id):
    """Eliminar un usuario por su ID"""
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM usuarios WHERE idUsuario = %s", (id,))
        connection.commit()
        if cursor.rowcount == 0:
            return jsonify({'error': 'Usuario no encontrado'}), 404
        return jsonify({'message': 'Usuario eliminado exitosamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()
