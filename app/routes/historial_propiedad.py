# app/routes/historial_propiedad.py
from flask import Blueprint, request, jsonify
from database.init_relational_db import get_db_connection

historial_propiedad_blueprint = Blueprint('historial_propiedad', __name__)

@historial_propiedad_blueprint.route('/historial', methods=['GET'])
def get_historial():
    """Obtener todo el historial de propiedad"""
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM historial_Propiedad")
        historial = cursor.fetchall()
        return jsonify(historial), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

@historial_propiedad_blueprint.route('/historial/<int:id>', methods=['GET'])
def get_historial_by_id(id):
    """Obtener un registro de historial por su ID"""
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM historial_Propiedad WHERE idHistorial = %s", (id,))
        registro = cursor.fetchone()
        if registro:
            return jsonify(registro), 200
        else:
            return jsonify({'error': 'Registro no encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

@historial_propiedad_blueprint.route('/historial', methods=['POST'])
def create_historial():
    """Crear un nuevo registro en el historial"""
    data = request.json
    idPersona = data.get('idPersona')
    idObjeto = data.get('idObjeto')
    FechaAdquisicion = data.get('FechaAdquisicion')
    FechaCambio = data.get('FechaCambio', None)
    
    if not all([idPersona, idObjeto, FechaAdquisicion]):
        return jsonify({'error': 'Todos los campos requeridos deben ser enviados'}), 400
    
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = """
        INSERT INTO historial_Propiedad (idPersona, idObjeto, FechaAdquisicion, FechaCambio)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (idPersona, idObjeto, FechaAdquisicion, FechaCambio))
        connection.commit()
        return jsonify({'message': 'Registro creado exitosamente'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

@historial_propiedad_blueprint.route('/historial/<int:id>', methods=['PUT'])
def update_historial(id):
    """Actualizar un registro del historial existente"""
    data = request.json
    FechaCambio = data.get('FechaCambio')
    
    if not FechaCambio:
        return jsonify({'error': 'FechaCambio es requerida para actualizar'}), 400
    
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        query = """
        UPDATE historial_Propiedad
        SET FechaCambio = %s
        WHERE idHistorial = %s
        """
        cursor.execute(query, (FechaCambio, id))
        connection.commit()
        if cursor.rowcount == 0:
            return jsonify({'error': 'Registro no encontrado'}), 404
        return jsonify({'message': 'Registro actualizado exitosamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()

@historial_propiedad_blueprint.route('/historial/<int:id>', methods=['DELETE'])
def delete_historial(id):
    """Eliminar un registro del historial por su ID"""
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM historial_Propiedad WHERE idHistorial = %s", (id,))
        connection.commit()
        if cursor.rowcount == 0:
            return jsonify({'error': 'Registro no encontrado'}), 404
        return jsonify({'message': 'Registro eliminado exitosamente'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if connection.is_connected():
            connection.close()
