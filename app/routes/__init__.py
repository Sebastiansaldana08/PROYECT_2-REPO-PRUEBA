from .home import home_blueprint
from .person import person_blueprint
from .hobbies import hobbies_blueprint
from .address import address_blueprint
from .item import item_blueprint
from .exchange import exchange_blueprint
from .rating import rating_blueprint
from .history import history_blueprint
from .wishlist import wishlist_blueprint
from .favorites import favorites_blueprint
from .comments import comments_blueprint
from .messages import messages_blueprint

def initialize_routes(app):
    app.register_blueprint(home_blueprint)
    app.register_blueprint(person_blueprint)  # Registrar las rutas de persona
    app.register_blueprint(hobbies_blueprint)  # Registrar las rutas de gustos
    app.register_blueprint(address_blueprint)  # Registrar las rutas de direcciones
    app.register_blueprint(item_blueprint)  # Registrar las rutas de objetos
    app.register_blueprint(exchange_blueprint)  # Registrar las rutas de intercambios
    app.register_blueprint(rating_blueprint)  # Registrar las rutas de calificaciones
    app.register_blueprint(history_blueprint)  # Registrar las rutas de historial
    app.register_blueprint(wishlist_blueprint)  # Registrar las rutas de lista de deseos
    app.register_blueprint(favorites_blueprint)  # Registrar las rutas de favoritos
    app.register_blueprint(comments_blueprint)  # Registrar las rutas de comentarios
    app.register_blueprint(messages_blueprint)  # Registrar las rutas de mensajes
    
    
    
    