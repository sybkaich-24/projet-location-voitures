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

    def create_agence(self, nom_agence, adresse, ville, code_postal, telephone):
        """Crée une nouvelle agence"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Construction de la requete avec utilisation de placeholerd pour éviter les injections SQL
                    query = "INSERT INTO agence (nom_agence, adresse, ville, code_postal, telephone) VALUES (%s, %s, %s, %s, %s)"
                    # Construction du tuple de parametres pour la requete
                    values = (nom_agence, adresse, ville, code_postal, telephone)
                    # Execution de la requete avec les parametres
                    cursor.execute(query, values)
                    # Validation de la transaction pour rendre definitif les modifications
                    connection.commit()
                    # Retour du resultat
                    return True
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return False
    
    def update_agence(self, id_agence, nom=None, adresse=None, ville=None, code_postal=None, telephone=None):
        """Met à jour une agence"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Construction de la requete avec utilisation de placeholerd pour éviter les injections SQL
                    query = "UPDATE agence SET "
                    # Construction du tuple de parametres pour la requete
                    values = []
                    if nom is not None:
                        query += "nom = %s, "
                        values.append(nom)
                    if adresse is not None:
                        query += "adresse = %s, "
                        values.append(adresse)
                    if ville is not None:
                        query += "ville = %s, "
                        values.append(ville)
                    if code_postal is not None:
                        query += "code_postal = %s, "
                        values.append(code_postal)
                    if telephone is not None:
                        query += "telephone = %s, "
                        values.append(telephone)
                    query = query.rstrip(", ")  # Remove the trailing comma and space
                    query += " WHERE id_agence = %s"
                    values.append(id_agence)
                    # Execution de la requete avec les parametres
                    cursor.execute(query, tuple(values))
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