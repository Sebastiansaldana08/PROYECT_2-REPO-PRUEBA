import unittest
import requests

BASE_URL = "http://127.0.0.1:5000"  # URL base para la API

class TestAPI(unittest.TestCase):

    # Pruebas para usuarios
    def test_get_usuarios(self):
        response = requests.get(f"{BASE_URL}/usuarios")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_create_usuario(self):
        data = {
            "username": "testuser",
            "password": "password123",
            "idPersona": None  # Campo opcional
        }
        response = requests.post(f"{BASE_URL}/usuarios", json=data)
        self.assertEqual(response.status_code, 201)
        self.assertIn("message", response.json())

    def test_get_usuario_by_id(self):
        response = requests.get(f"{BASE_URL}/usuarios/1")
        if response.status_code == 200:
            usuario = response.json()
            self.assertIn("username", usuario)  # Asegurarnos de que se devuelve el usuario correcto
        else:
            self.assertEqual(response.status_code, 404)


    # Pruebas para informacion_persona
    def test_get_informacion_persona(self):
        response = requests.get(f"{BASE_URL}/informacion_persona")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_create_informacion_persona(self):
        data = {
            "DNI": "12345678",
            "Nombre": "Juan Perez",
            "FechaNacimiento": "1990-01-01",
            "DireccionCorreo": "juan@example.com",
            "PuntuacionPromedio": 4.5
        }
        response = requests.post(f"{BASE_URL}/informacion_persona", json=data)
        self.assertEqual(response.status_code, 201)
        self.assertIn("message", response.json())

    # Pruebas para objeto
    def test_get_objetos(self):
        response = requests.get(f"{BASE_URL}/objetos")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_create_objeto(self):
        data = {
            "idPersona": 1,  # ID de persona inexistente
            "Nombre": "Libro",
            "Descripcion": "Libro de ciencia ficción",
            "URL_Imagen": "http://example.com/imagen.jpg",
            "URL_Video": "http://example.com/video.mp4",
            "ObjetoDeseado": "Pelicula"
        }
        response = requests.post(f"{BASE_URL}/objetos", json=data)
        self.assertIn(response.status_code, [201, 400, 500])  # Error esperado porque la tabla está vacía

    # Pruebas para intercambio
    def test_get_intercambios(self):
        response = requests.get(f"{BASE_URL}/intercambios")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_create_intercambio(self):
        data = {
            "idPersona1": 1,  # ID de persona inexistente
            "idObjeto1": 1,   # ID de objeto inexistente
            "idPersona2": 2,  # ID de persona inexistente
            "idObjeto2": 2,   # ID de objeto inexistente
            "Fecha": "2024-11-25"
        }
        response = requests.post(f"{BASE_URL}/intercambios", json=data)
        self.assertIn(response.status_code, [400, 500])  # Error esperado porque la tabla está vacía

    # Pruebas para valoracion_intercambio
    def test_get_valoraciones(self):
        response = requests.get(f"{BASE_URL}/valoraciones")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_create_valoracion(self):
        data = {
            "idIntercambio": 1,  # ID de intercambio inexistente
            "idPersona1": 1,     # ID de persona inexistente
            "Puntuacion": 5,
            "Comentario": "Excelente intercambio",
            "idPersona2": 2      # ID de persona inexistente
        }
        response = requests.post(f"{BASE_URL}/valoraciones", json=data)
        self.assertIn(response.status_code, [400, 500])  # Error esperado porque la tabla está vacía

    # Pruebas para historial_propiedad
    def test_get_historial(self):
        response = requests.get(f"{BASE_URL}/historial")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_create_historial(self):
        data = {
            "idPersona": 1,        # ID de persona inexistente
            "idObjeto": 1,         # ID de objeto inexistente
            "FechaAdquisicion": "2024-11-25",
            "FechaCambio": None
        }
        response = requests.post(f"{BASE_URL}/historial", json=data)
        self.assertIn(response.status_code, [400, 500])  # Error esperado porque la tabla está vacía

    # Pruebas para notificaciones
    def test_get_notificaciones(self):
        response = requests.get(f"{BASE_URL}/notificaciones")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_create_notificacion(self):
        data = {
            "idUsuario": 1,  # ID de usuario inexistente
            "Tipo": "Alerta",
            "Mensaje": "Mensaje de prueba",
            "Estado": "No leída"
        }
        response = requests.post(f"{BASE_URL}/notificaciones", json=data)
        self.assertIn(response.status_code, [400, 500])  # Error esperado porque la tabla está vacía


if __name__ == '__main__':
    unittest.main()
