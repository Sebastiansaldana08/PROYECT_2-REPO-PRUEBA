from neo4j import GraphDatabase

class Neo4jDatabase:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
    
    def close(self):
        self.driver.close()
    
    def execute_query(self, query, parameters=None):
        with self.driver.session() as session:
            return session.run(query, parameters or {}).data()

# Configuración de conexión a Neo4j
neo4j_db = Neo4jDatabase(
    uri="bolt://3.84.188.201:7687",
    user="neo4j",
    password="spare-competition-surveillance"
)
