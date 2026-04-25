import mysql.connector
from mysql.connector import Error

class Agent_d_agenceDAO:
    """
    Classe d'acces et de gestion des agents d'agence dans la base de données DAO

    id_employe INT,
    description_role TEXT,
    salaire DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (id_employe),
    FOREIGN KEY (id_employe) REFERENCES Employe(id_employe)

    Herite de l'entite Employe
    """
    def __init__(self, host, user, password, database, port):
        self.config = {
            'host': host,
            'user': user,
            'password': password,
            'database': database,
            'port': port
        }

    def get_agent_d_agence_by_id(self, id_employe):
        """Récupère un agent d'agence par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT * FROM agent_d_agence WHERE id_employe = %s"
                    # Parametres
                    value = (id_employe,)
                    # Execution 
                    cursor.execute(query, value)
                    # Resultat
                    result = cursor.fetchone()
                    # Retour
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_all_agents_d_agence(self):
        """Récupère tous les agents d'agence"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT * FROM agent_d_agence"
                    # Execution 
                    cursor.execute(query)
                    # Resultat
                    result = cursor.fetchall()
                    # Retour
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_salaire_agent_d_agence_by_id(self, id_employe):
        """Récupère le salaire d'un employe par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT salaire FROM agent_d_agence WHERE id_employe = %s"
                    # Parametres
                    value = (id_employe,)
                    # Execution 
                    cursor.execute(query, value)
                    # Resultat
                    result = cursor.fetchone()
                    # Retour
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_description_role_agent_d_agence_by_id(self, id_employe):
        """Récupère la description du rôle d'un employe par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT description_role FROM agent_d_agence WHERE id_employe = %s"
                    # Parametres
                    value = (id_employe,)
                    # Execution 
                    cursor.execute(query, value)
                    # Resultat
                    result = cursor.fetchone()
                    # Retour
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def create_agent_d_agence(self, id_employe, description_role, salaire):
        """Crée un agent d'agence"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "INSERT INTO agent_d_agence (id_employe, description_role, salaire) VALUES (%s, %s, %s)"
                    # Parametres
                    values = (id_employe, description_role, salaire)
                    # Execution 
                    cursor.execute(query, values)
                    connection.commit()
                    # Resultat
                    result = cursor.lastrowid
                    # Retour
                    return cursor.lastrowid
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def update_agent_d_agence(self, id_employe, description_role=None, salaire=None):
        """Met à jour un agent d'agence"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "UPDATE agent_d_agence SET description_role = COALESCE(%s, description_role), salaire = COALESCE(%s, salaire) WHERE id_employe = %s"
                    # Parametres
                    values = (description_role, salaire, id_employe)
                    # Execution 
                    cursor.execute(query, values)
                    # Commit pour sauvegarder les changements
                    connection.commit()
                    # Retour
                    return True
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return False
        
    def delete_agent_d_agence(self, id_employe):
        """Supprime un agent d'agence par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "DELETE FROM agent_d_agence WHERE id_employe = %s"
                    # Parametres
                    value = (id_employe,)
                    # Execution 
                    cursor.execute(query, value)
                    # Commit pour sauvegarder les changements
                    connection.commit()
                    # Retour
                    return True
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return False