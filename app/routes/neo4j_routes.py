from flask import Blueprint, jsonify, request
from database.init_neo4j_db import neo4j_db

neo4j_blueprint = Blueprint('neo4j', __name__)

# Crear un nodo Usuario
@neo4j_blueprint.route('/neo4j/usuarios', methods=['POST'])
def create_usuario():
    data = request.json
    query = """
    CREATE (:Usuario {idUsuario: $idUsuario, username: $username, puntuacionPromedio: $puntuacionPromedio})
    """
    parameters = {
        "idUsuario": data.get("idUsuario"),
        "username": data.get("username"),
        "puntuacionPromedio": data.get("puntuacionPromedio")
    }
    neo4j_db.execute_query(query, parameters)
    return jsonify({"message": "Usuario creado exitosamente"}), 201

# Obtener todos los nodos Usuario
@neo4j_blueprint.route('/neo4j/usuarios', methods=['GET'])
def get_usuarios():
    query = "MATCH (u:Usuario) RETURN u"
    result = neo4j_db.execute_query(query)
    return jsonify(result), 200

# Crear un nodo Objeto
@neo4j_blueprint.route('/neo4j/objetos', methods=['POST'])
def create_objeto():
    data = request.json
    query = """
    CREATE (:Objeto {idObjeto: $idObjeto, nombre: $nombre, descripcion: $descripcion, estado: $estado, objetoDeseado: $objetoDeseado})
    """
    parameters = {
        "idObjeto": data.get("idObjeto"),
        "nombre": data.get("nombre"),
        "descripcion": data.get("descripcion"),
        "estado": data.get("estado"),
        "objetoDeseado": data.get("objetoDeseado")
    }
    neo4j_db.execute_query(query, parameters)
    return jsonify({"message": "Objeto creado exitosamente"}), 201

# Crear una relación OFRECE entre Usuario y Objeto
@neo4j_blueprint.route('/neo4j/relaciones/ofrece', methods=['POST'])
def create_ofrece_relation():
    data = request.json
    query = """
    MATCH (u:Usuario {idUsuario: $idUsuario}), (o:Objeto {idObjeto: $idObjeto})
    CREATE (u)-[:OFRECE]->(o)
    """
    parameters = {
        "idUsuario": data.get("idUsuario"),
        "idObjeto": data.get("idObjeto")
    }
    neo4j_db.execute_query(query, parameters)
    return jsonify({"message": "Relación OFRECE creada exitosamente"}), 201

# Crear una relación DESEA entre Usuario y Objeto
@neo4j_blueprint.route('/neo4j/relaciones/desea', methods=['POST'])
def create_desea_relation():
    data = request.json
    query = """
    MATCH (u:Usuario {idUsuario: $idUsuario}), (o:Objeto {idObjeto: $idObjeto})
    CREATE (u)-[:DESEA]->(o)
    """
    parameters = {
        "idUsuario": data.get("idUsuario"),
        "idObjeto": data.get("idObjeto")
    }
    neo4j_db.execute_query(query, parameters)
    return jsonify({"message": "Relación DESEA creada exitosamente"}), 201

# Crear un nodo Intercambio
@neo4j_blueprint.route('/neo4j/intercambios', methods=['POST'])
def create_intercambio():
    data = request.json
    query = """
    CREATE (:Intercambio {idIntercambio: $idIntercambio, fecha: $fecha, estado: $estado})
    """
    parameters = {
        "idIntercambio": data.get("idIntercambio"),
        "fecha": data.get("fecha"),
        "estado": data.get("estado")
    }
    neo4j_db.execute_query(query, parameters)
    return jsonify({"message": "Intercambio creado exitosamente"}), 201

# Crear una relación PROPUSO entre Usuario e Intercambio
@neo4j_blueprint.route('/neo4j/relaciones/propuso', methods=['POST'])
def create_propuso_relation():
    data = request.json
    query = """
    MATCH (u:Usuario {idUsuario: $idUsuario}), (i:Intercambio {idIntercambio: $idIntercambio})
    CREATE (u)-[:PROPUSO]->(i)
    """
    parameters = {
        "idUsuario": data.get("idUsuario"),
        "idIntercambio": data.get("idIntercambio")
    }
    neo4j_db.execute_query(query, parameters)
    return jsonify({"message": "Relación PROPUSO creada exitosamente"}), 201

# Crear una relación PARTICIPÓ_EN entre Usuario e Intercambio
@neo4j_blueprint.route('/neo4j/relaciones/participo_en', methods=['POST'])
def create_participo_en_relation():
    data = request.json
    query = """
    MATCH (u:Usuario {idUsuario: $idUsuario}), (i:Intercambio {idIntercambio: $idIntercambio})
    CREATE (u)-[:PARTICIPÓ_EN]->(i)
    """
    parameters = {
        "idUsuario": data.get("idUsuario"),
        "idIntercambio": data.get("idIntercambio")
    }
    neo4j_db.execute_query(query, parameters)
    return jsonify({"message": "Relación PARTICIPÓ_EN creada exitosamente"}), 201

# Crear un nodo Valoracion
@neo4j_blueprint.route('/neo4j/valoraciones', methods=['POST'])
def create_valoracion():
    data = request.json
    query = """
    CREATE (:Valoracion {idValoracion: $idValoracion, puntuacion: $puntuacion, comentario: $comentario})
    """
    parameters = {
        "idValoracion": data.get("idValoracion"),
        "puntuacion": data.get("puntuacion"),
        "comentario": data.get("comentario")
    }
    neo4j_db.execute_query(query, parameters)
    return jsonify({"message": "Valoración creada exitosamente"}), 201

# Crear una relación VALORÓ entre Usuario y Valoracion
@neo4j_blueprint.route('/neo4j/relaciones/valoro', methods=['POST'])
def create_valoro_relation():
    data = request.json
    query = """
    MATCH (u:Usuario {idUsuario: $idUsuario}), (v:Valoracion {idValoracion: $idValoracion})
    CREATE (u)-[:VALORÓ]->(v)
    """
    parameters = {
        "idUsuario": data.get("idUsuario"),
        "idValoracion": data.get("idValoracion")
    }
    neo4j_db.execute_query(query, parameters)
    return jsonify({"message": "Relación VALORÓ creada exitosamente"}), 201

# Crear un nodo Notificacion
@neo4j_blueprint.route('/neo4j/notificaciones', methods=['POST'])
def create_notificacion():
    data = request.json
    query = """
    CREATE (:Notificacion {idNotificacion: $idNotificacion, tipo: $tipo, mensaje: $mensaje, estado: $estado})
    """
    parameters = {
        "idNotificacion": data.get("idNotificacion"),
        "tipo": data.get("tipo"),
        "mensaje": data.get("mensaje"),
        "estado": data.get("estado")
    }
    neo4j_db.execute_query(query, parameters)
    return jsonify({"message": "Notificación creada exitosamente"}), 201

# Crear una relación NOTIFICADO entre Notificacion y Usuario
@neo4j_blueprint.route('/neo4j/relaciones/notificado', methods=['POST'])
def create_notificado_relation():
    data = request.json
    query = """
    MATCH (n:Notificacion {idNotificacion: $idNotificacion}), (u:Usuario {idUsuario: $idUsuario})
    CREATE (n)-[:NOTIFICADO]->(u)
    """
    parameters = {
        "idNotificacion": data.get("idNotificacion"),
        "idUsuario": data.get("idUsuario")
    }
    neo4j_db.execute_query(query, parameters)
    return jsonify({"message": "Relación NOTIFICADO creada exitosamente"}), 201
