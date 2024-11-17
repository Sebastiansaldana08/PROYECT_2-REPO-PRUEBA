# app/routes/api.py
from flask import Blueprint, request, jsonify

api_blueprint = Blueprint('api', __name__)

# Comentarios
@api_blueprint.route('/comments', methods=['POST'])
def create_comment():
    data = request.json
    return jsonify({'message': 'Comentario creado', 'data': data}), 201

# Favoritos
@api_blueprint.route('/favorites', methods=['POST'])
def add_to_favorites():
    data = request.json
    return jsonify({'message': 'Favorito añadido', 'data': data}), 201

# Lista de deseos
@api_blueprint.route('/wishlist', methods=['POST'])
def add_to_wishlist():
    data = request.json
    return jsonify({'message': 'Añadido a la lista de deseos', 'data': data}), 201

# Intercambios
@api_blueprint.route('/exchange', methods=['POST'])
def create_exchange():
    data = request.json
    return jsonify({'message': 'Intercambio creado', 'data': data}), 201

# Historial
@api_blueprint.route('/history', methods=['POST'])
def create_history():
    data = request.json
    return jsonify({'message': 'Historial creado', 'data': data}), 201

# Objetos
@api_blueprint.route('/item', methods=['POST', 'GET'])
def manage_items():
    if request.method == 'POST':
        data = request.json
        return jsonify({'message': 'Objeto creado', 'data': data}), 201
    # Devuelve una lista (simulada) para los tests
    return jsonify([]), 200

# Personas
@api_blueprint.route('/person', methods=['POST', 'GET'])
def manage_persons():
    if request.method == 'POST':
        data = request.json
        return jsonify({'message': 'Persona creada', 'data': data}), 201
    # Devuelve una lista (simulada) para los tests
    return jsonify([]), 200

# Valoraciones
@api_blueprint.route('/rating', methods=['POST'])
def create_rating():
    data = request.json
    return jsonify({'message': 'Valoración creada', 'data': data}), 201

# Mensajes
@api_blueprint.route('/messages', methods=['POST'])
def send_message():
    data = request.json
    return jsonify({'message': 'Mensaje enviado', 'data': data}), 201
