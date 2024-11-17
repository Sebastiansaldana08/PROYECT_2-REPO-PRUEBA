import unittest
import requests

BASE_URL = "http://127.0.0.1:5000/api"

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.headers = {'Content-Type': 'application/json'}

    # Usuarios
    def test_create_person(self):
        payload = {
            "DNI": "12345678",
            "Nombre": "Juan Pérez",
            "FechaNacimiento": "1990-01-01",
            "DireccionCorreo": "juan@example.com"
        }
        response = requests.post(f"{BASE_URL}/person", json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 201)

    def test_get_all_persons(self):
        response = requests.get(f"{BASE_URL}/person", headers=self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    # Objetos
    def test_create_item(self):
        payload = {
            "idPersona": 1,
            "Nombre": "Bicicleta",
            "Descripcion": "Bicicleta de montaña",
            "URL_Imagen": "http://example.com/bike.jpg",
            "URL_Video": "http://example.com/bike.mp4",
            "ObjetoDeseado": "Patines"
        }
        response = requests.post(f"{BASE_URL}/item", json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 201)

    def test_get_all_items(self):
        response = requests.get(f"{BASE_URL}/item", headers=self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    # Intercambios
    def test_create_exchange(self):
        payload = {
            "idPersona1": 1,
            "idObjeto1": 1,
            "idPersona2": 2,
            "idObjeto2": 2,
            "Fecha": "2024-01-01"
        }
        response = requests.post(f"{BASE_URL}/exchange", json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 201)

    # Valoraciones
    def test_create_rating(self):
        payload = {
            "idIntercambio": 1,
            "idPersona1": 1,
            "Puntuacion": 5,
            "Comentario": "Buen intercambio",
            "idPersona2": 2,
            "Fecha": "2024-01-02 12:00:00"
        }
        response = requests.post(f"{BASE_URL}/rating", json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 201)

    # Historial de Propiedad
    def test_create_history(self):
        payload = {
            "idPersona": 1,
            "idObjeto": 1,
            "FechaAdquisicion": "2024-01-01",
            "FechaCambio": None
        }
        response = requests.post(f"{BASE_URL}/history", json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 201)

    # Lista de Deseos
    def test_add_to_wishlist(self):
        payload = {
            "idPersona": 1,
            "idObjetoDeseado": 2
        }
        response = requests.post(f"{BASE_URL}/wishlist", json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 201)

    # Favoritos
    def test_add_to_favorites(self):
        payload = {
            "idPersona": 1,
            "idObjetoFavorito": 2
        }
        response = requests.post(f"{BASE_URL}/favorites", json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 201)

    # Comentarios
    def test_add_comment(self):
        payload = {
            "idIntercambio": 1,
            "idPersona": 1,
            "Comentario": "Muy buen trato",
            "Fecha": "2024-01-02 12:00:00"
        }
        response = requests.post(f"{BASE_URL}/comments", json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 201)

    # Mensajes
    def test_send_message(self):
        payload = {
            "idPersonaRemitente": 1,
            "idPersonaDestinatario": 2,
            "Mensaje": "¿Intercambiamos?",
            "Fecha": "2024-01-02 13:00:00"
        }
        response = requests.post(f"{BASE_URL}/messages", json=payload, headers=self.headers)
        self.assertEqual(response.status_code, 201)


if __name__ == "__main__":
    unittest.main()
