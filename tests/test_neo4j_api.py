import unittest
import requests

BASE_URL = "http://127.0.0.1:5000"  # URL base para la API

class TestNeo4jAPI(unittest.TestCase):

    # Pruebas para Usuario
    def test_create_usuario(self):
        data = {
            "idUsuario": 1,
            "username": "usuario1",
            "puntuacionPromedio": 4.5
        }
        response = requests.post(f"{BASE_URL}/neo4j/usuarios", json=data)
        self.assertEqual(response.status_code, 201)
        self.assertIn("message", response.json())

    def test_get_usuarios(self):
        response = requests.get(f"{BASE_URL}/neo4j/usuarios")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    # Pruebas para Objeto
    def test_create_objeto(self):
        data = {
            "idObjeto": 1,
            "nombre": "Bicicleta",
            "descripcion": "Bicicleta de montaña",
            "estado": "Disponible",
            "objetoDeseado": "Patineta"
        }
        response = requests.post(f"{BASE_URL}/neo4j/objetos", json=data)
        self.assertEqual(response.status_code, 201)
        self.assertIn("message", response.json())

    def test_create_ofrece_relation(self):
        data = {
            "idUsuario": 1,
            "idObjeto": 1
        }
        response = requests.post(f"{BASE_URL}/neo4j/relaciones/ofrece", json=data)
        self.assertEqual(response.status_code, 201)
        self.assertIn("message", response.json())

    def test_create_desea_relation(self):
        data = {
            "idUsuario": 1,
            "idObjeto": 1
        }
        response = requests.post(f"{BASE_URL}/neo4j/relaciones/desea", json=data)
        self.assertEqual(response.status_code, 201)
        self.assertIn("message", response.json())

    # Pruebas para Intercambio
    def test_create_intercambio(self):
        data = {
            "idIntercambio": 1,
            "fecha": "2024-11-25",
            "estado": "Pendiente"
        }
        response = requests.post(f"{BASE_URL}/neo4j/intercambios", json=data)
        self.assertEqual(response.status_code, 201)
        self.assertIn("message", response.json())

    def test_create_propuso_relation(self):
        data = {
            "idUsuario": 1,
            "idIntercambio": 1
        }
        response = requests.post(f"{BASE_URL}/neo4j/relaciones/propuso", json=data)
        self.assertEqual(response.status_code, 201)
        self.assertIn("message", response.json())

    def test_create_participo_en_relation(self):
        data = {
            "idUsuario": 1,
            "idIntercambio": 1
        }
        response = requests.post(f"{BASE_URL}/neo4j/relaciones/participo_en", json=data)
        self.assertEqual(response.status_code, 201)
        self.assertIn("message", response.json())

    # Pruebas para Valoracion
    def test_create_valoracion(self):
        data = {
            "idValoracion": 1,
            "puntuacion": 5,
            "comentario": "Excelente intercambio"
        }
        response = requests.post(f"{BASE_URL}/neo4j/valoraciones", json=data)
        self.assertEqual(response.status_code, 201)
        self.assertIn("message", response.json())

    def test_create_valoro_relation(self):
        data = {
            "idUsuario": 1,
            "idValoracion": 1
        }
        response = requests.post(f"{BASE_URL}/neo4j/relaciones/valoro", json=data)
        self.assertEqual(response.status_code, 201)
        self.assertIn("message", response.json())

    # Pruebas para Notificacion
    def test_create_notificacion(self):
        data = {
            "idNotificacion": 1,
            "tipo": "Propuesta",
            "mensaje": "Intercambio propuesto",
            "estado": "No Leída"
        }
        response = requests.post(f"{BASE_URL}/neo4j/notificaciones", json=data)
        self.assertEqual(response.status_code, 201)
        self.assertIn("message", response.json())

    def test_create_notificado_relation(self):
        data = {
            "idNotificacion": 1,
            "idUsuario": 1
        }
        response = requests.post(f"{BASE_URL}/neo4j/relaciones/notificado", json=data)
        self.assertEqual(response.status_code, 201)
        self.assertIn("message", response.json())

if __name__ == '__main__':
    unittest.main()
