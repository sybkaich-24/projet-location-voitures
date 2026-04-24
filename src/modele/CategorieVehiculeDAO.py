import mysql.connector
from mysql.connector import Error

class CategorieVehiculeDAO:
    def __init__(self, host, user, password, database):
        self.config = {
            'host': host,
            'user': user,
            'password': password,
            'database': database,
            'port': 3307 
        }
    
    def get_categorie_vehicule_by_id(self, id_categorie):
        """Récupère une catégorie de véhicule par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT * FROM categorie_vehicule WHERE id_categorie = %s"
                    # Parametres
                    value = (id_categorie,)
                    # Execution 
                    cursor.execute(query, value)
                    # Resultat
                    result = cursor.fetchone()
                    # Retour
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_id_categorie_by_nom(self, nom):
        """Récupère l'ID d'une catégorie de véhicule par son nom"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT id_categorie FROM categorie_vehicule WHERE nom = %s"
                    # Parametres
                    value = (nom,)
                    # Execution 
                    cursor.execute(query, value)
                    # Resultat
                    result = cursor.fetchone()
                    # Retour
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
    
    def get_all_categorie_vehicules(self):
        """Récupère toutes les catégories de véhicules"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT * FROM categorie_vehicule"
                    # Execution 
                    cursor.execute(query)
                    # Resultat
                    result = cursor.fetchall()
                    # Retour
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def create_categorie_vehicule(self, nom):
        """Crée une nouvelle catégorie de véhicule"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "INSERT INTO categorie_vehicule (nom) VALUES (%s)"
                    # Parametres
                    value = (nom,)
                    # Execution 
                    cursor.execute(query, value)
                    # Commit pour sauvegarder les changements
                    connection.commit()
                    # Retour
                    return True
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return False
        
    def update_categorie_vehicule(self, id_categorie, nom):
        """Met à jour une catégorie de véhicule"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "UPDATE categorie_vehicule SET nom = %s WHERE id_categorie = %s"
                    # Parametres
                    values = (nom, id_categorie)
                    # Execution 
                    cursor.execute(query, values)
                    # Commit pour sauvegarder les changements
                    connection.commit()
                    # Retour
                    return True
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return False
        
    def delete_categorie_vehicule(self, id_categorie):
        """Supprime une catégorie de véhicule par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "DELETE FROM categorie_vehicule WHERE id_categorie = %s"
                    # Parametres
                    value = (id_categorie,)
                    # Execution 
                    cursor.execute(query, value)
                    # Commit pour sauvegarder les changements
                    connection.commit()
                    # Retour
                    return True
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return False