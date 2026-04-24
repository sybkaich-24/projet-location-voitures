import mysql.connector
from mysql.connector import Error

class AgenceDAO:
    def __init__(self, host, user, password, database):
        self.config = {
            'host': host,
            'user': user,
            'password': password,
            'database': database,
            'port': 3307 # Il faut s'assurer que le port de docker est le meme 
        }

    def get_agence_by_id(self, id_agence):
        """Récupère une agence par son ID"""

        # Connexion automatique grace a l'utilisation du bloc with gerant la déconnextion
        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Construction de la requete avec utilisation de placeholerd pour éviter les injections SQL
                    query = "SELECT * FROM agence WHERE id_agence = %s"
                    # Construction du tuple de parametres pour la requete
                    value = (id_agence,)
                    # Execution de la requete avec les parametres
                    cursor.execute(query, value)
                    # Récupération du resultat
                    result = cursor.fetchone()
                    # Retour du resultat
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_all_agences(self):
        """Récupère toutes les agences"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Construction de la requete
                    query = "SELECT * FROM agence"
                    # Execution de la requete
                    cursor.execute(query)
                    # Récupération du resultat
                    result = cursor.fetchall()
                    # Retour du resultat
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def create_agence(self, nom, adresse):
        """Crée une nouvelle agence"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Construction de la requete avec utilisation de placeholerd pour éviter les injections SQL
                    query = "INSERT INTO agence (nom, adresse) VALUES (%s, %s)"
                    # Construction du tuple de parametres pour la requete
                    values = (nom, adresse)
                    # Execution de la requete avec les parametres
                    cursor.execute(query, values)
                    # Validation de la transaction pour rendre definitif les modifications
                    connection.commit()
                    # Retour du resultat
                    return True
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return False
    
    def update_agence(self, id_agence, nom, adresse):
        """Met à jour une agence"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Construction de la requete avec utilisation de placeholerd pour éviter les injections SQL
                    query = "UPDATE agence SET nom = %s, adresse = %s WHERE id_agence = %s"
                    # Construction du tuple de parametres pour la requete
                    values = (nom, adresse, id_agence)
                    # Execution de la requete avec les parametres
                    cursor.execute(query, values)
                    # Validation de la transaction pour rendre definitif les modifications
                    connection.commit()
                    # Retour du resultat
                    return True
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return False
        
    def delete_agence_by_id(self, id_agence):
        """Supprime une agence par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Construction de la requete avec utilisation de placeholerd pour éviter les injections SQL
                    query = "DELETE FROM agence WHERE id_agence = %s"
                    # Construction du tuple de parametres pour la requete
                    value = (id_agence,) # Il faut s'assurer que le tuple contient une virgule pour être considéré comme un tuple d'un seul élément
                    # Execution de la requete avec les parametres
                    cursor.execute(query, value)
                    # Validation de la transaction pour rendre definitif les modifications
                    connection.commit()
                    # Retour du resultat
                    return True
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return False