import mysql.connector
from mysql.connector import Error

class ComptableDAO:
    """
    Classe d'acces et de gestion des comptables dans la base de données DAO
    
    id_employe INT,
    description_role TEXT,
    salaire DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (id_employe),
    FOREIGN KEY (id_employe) REFERENCES Employe(id_employe)

    Herite de l'entite Employe
    """
    def __init__(self, host, user, password, database):
        self.config = {
            'host': host,
            'user': user,
            'password': password,
            'database': database,
            'port': 3307 # Il faut s'assurer que le port de docker est le meme 
        }

    def get_comptable_by_id(self, id_employe):
        """Récupère un comptable par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT * FROM comptable WHERE id_employe = %s"
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
        
    def get_all_comptables(self):
        """Récupère tous les comptables"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT * FROM comptable"
                    # Execution 
                    cursor.execute(query)
                    # Resultat
                    result = cursor.fetchall()
                    # Retour
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_salaire_comptable_by_id(self, id_employe):
        """Récupère le salaire d'un employe par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT salaire FROM comptable WHERE id_employe = %s"
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
        
    def get_description_role_comptable_by_id(self, id_employe):
        """Récupère la description du role d'un comptable par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT description_role FROM comptable WHERE id_employe = %s"
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
        
    def create_comptable(self, id_employe, description_role, salaire):
        """Crée un nouveau comptable"""
        
        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "INSERT INTO comptable (id_employe, description_role, salaire) VALUES (%s, %s, %s)"
                    # Parametres
                    values = (id_employe, description_role, salaire)
                    # Execution 
                    cursor.execute(query, values)
                    # Commit pour sauvegarder les changements
                    connection.commit()
                    # Retour
                    return cursor.lastrowid
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def update_comptable(self, id_employe, description_role=None, salaire=None):
        """Met à jour un comptable existant"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête
                    query = "UPDATE comptable SET description_role = COALESCE(%s, description_role), salaire = COALESCE(%s, salaire) WHERE id_employe = %s"
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
        
    def delete_comptable(self, id_employe):
        """Supprime le profile comptable d'un employe"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête
                    query = "DELETE FROM comptable WHERE id_employe = %s"
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
