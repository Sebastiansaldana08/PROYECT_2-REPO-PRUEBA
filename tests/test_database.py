# tests/test_database.py
import unittest
from database.init_relational_db import get_db_connection

class TestDatabaseConnection(unittest.TestCase):
    def test_connection(self):
        connection = None  # Asegurarse de que connection esté inicializado
        try:
            connection = get_db_connection()
            self.assertTrue(connection.is_connected())  # Verifica si la conexión es exitosa
            print("Conexión a la base de datos exitosa.")
        except Exception as e:
            self.fail(f"No se pudo conectar a la base de datos. Error: {e}")
        finally:
            if connection and connection.is_connected():  # Solo cierra si la conexión existe
                connection.close()

if __name__ == '__main__':
    unittest.main()
