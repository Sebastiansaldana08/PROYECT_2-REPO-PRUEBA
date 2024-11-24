# app/routes/intercambio.py
from flask import Blueprint, request, jsonify
from database.init_relational_db import get_db_connection

intercambio_blueprint = Blueprint('intercambio', __name__)

@intercambio_blueprint.route('/intercambios', methods=['GET'])
def get_intercambios():
    """Obtener todos los intercambios"""
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Intercambio")
        intercambios = cursor.fetchall()
        return jsonify(intercambios), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

@intercambio_blueprint.route('/intercambios/<int:id>', methods=['GET'])
def get_intercambio_by_id(id):
    """Obtener un intercambio por su ID"""
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Intercambio WHERE idIntercambio = %s", (id,))
        intercambio = cursor.fetchone()
        if intercambio:
            return jsonify(intercambio), 200
        else:
            return jsonify({'error': 'Intercambio no encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

@intercambio_blueprint.route('/intercambios', methods=['POST'])
def create_intercambio():
    """Crear un nuevo intercambio"""
    data = request.json
    idPersona1 = data.get('idPersona1')
    idObjeto1 = data.get('idObjeto1')
    idPersona2 = data.get('idPersona2')
    idObjeto2 = data.get('idObjeto2')
    Fecha = data.get('Fecha')
    Estado = data.get('Estado', 'Pendiente')  # Estado por defecto: Pendiente
    
    if not all([idPersona1, idObjeto1, idPersona2, idObjeto2, Fecha]):
        return jsonify({'error': 'Todos los campos requeridos deben ser enviados'}), 400
    
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = """
        INSERT INTO Intercambio (idPersona1, idObjeto1, idPersona2, idObjeto2, Fecha, Estado)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (idPersona1, idObjeto1, idPersona2, idObjeto2, Fecha, Estado))
        connection.commit()
        return jsonify({'message': 'Intercambio creado exitosamente'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

@intercambio_blueprint.route('/intercambios/<int:id>', methods=['PUT'])
def update_intercambio(id):
    """Actualizar un intercambio existente"""
    data = request.json
    Estado = data.get('Estado')
    Fecha = data.get('Fecha')
    
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = """
        UPDATE Intercambio
        SET Estado = %s, Fecha = %s
        WHERE idIntercambio = %s
        """
        cursor.execute(query, (Estado, Fecha, id))
        connection.commit()
        if cursor.rowcount == 0:
            return jsonify({'error': 'Intercambio no encontrado'}), 404
        return jsonify({'message': 'Intercambio actualizado exitosamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

@intercambio_blueprint.route('/intercambios/<int:id>', methods=['DELETE'])
def delete_intercambio(id):
    """Eliminar un intercambio por su ID"""
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM Intercambio WHERE idIntercambio = %s", (id,))
        connection.commit()
        if cursor.rowcount == 0:
            return jsonify({'error': 'Intercambio no encontrado'}), 404
        return jsonify({'message': 'Intercambio eliminado exitosamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()
