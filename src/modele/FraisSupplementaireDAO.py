import mysql.connector
from mysql.connector import Error

class FraisSupplementaireDAO:
    def __init__(self, host, user, password, database):
        self.config = {
            'host': host,
            'user': user,
            'password': password,
            'database': database,
            'port': 3307 # Il faut s'assurer que le port de docker est le meme 
        }

    def get_frais_supplementaires_by_id(self, id_frais_supplementaires):
        """Récupère les frais supplémentaires par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT * FROM frais_supplementaires WHERE id_frais_supplementaires = %s"
                    # Parametres
                    value = (id_frais_supplementaires,)
                    # Execution 
                    cursor.execute(query, value)
                    # Resultat
                    result = cursor.fetchone()
                    # Retour
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_all_frais_supplementaires(self):
        """Récupère tous les frais supplémentaires"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT * FROM frais_supplementaires"
                    # Execution 
                    cursor.execute(query)
                    # Resultat
                    result = cursor.fetchall()
                    # Retour
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_montant_frais_supplementaires_by_id(self, id_frais_supplementaires):
        """Récupère le montant des frais supplémentaires par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT montant FROM frais_supplementaires WHERE id_frais_supplementaires = %s"
                    # Parametres
                    value = (id_frais_supplementaires,)
                    # Execution 
                    cursor.execute(query, value)
                    # Resultat
                    result = cursor.fetchone()
                    # Retour
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_description_frais_supplementaires_by_id(self, id_frais_supplementaires):
        """Récupère la description des frais supplémentaires par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT description FROM frais_supplementaires WHERE id_frais_supplementaires = %s"
                    # Parametres
                    value = (id_frais_supplementaires,)
                    # Execution 
                    cursor.execute(query, value)
                    # Resultat
                    result = cursor.fetchone()
                    # Retour
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
    
    def create_frais_supplementaires(self, type_frais, montant, description, date_frais, id_location):
        """Crée un frais supplémentaire"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "INSERT INTO frais_supplementaires (type_frais, montant, description, date_frais, id_location) VALUES (%s, %s, %s, %s, %s)"
                    # Parametres
                    values = (type_frais, montant, description, date_frais, id_location)
                    # Execution 
                    cursor.execute(query, values)
                    connection.commit()
                    # Retour
                    return True
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return False
        
    def update_frais_supplementaires(self, id_frais_supplementaires, type_frais=None, montant=None, description=None, date_frais=None, id_location=None):
        """Met à jour un frais supplémentaire"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Construction de la requête de mise à jour
                    query = "UPDATE frais_supplementaires SET "
                    values = []
                    if type_frais is not None:
                        query += "type_frais = %s, "
                        values.append(type_frais)
                    if montant is not None:
                        query += "montant = %s, "
                        values.append(montant)
                    if description is not None:
                        query += "description = %s, "
                        values.append(description)
                    if date_frais is not None:
                        query += "date_frais = %s, "
                        values.append(date_frais)
                    if id_location is not None:
                        query += "id_location = %s, "
                        values.append(id_location)
                    
                    # Retirer la dernière virgule et ajouter la condition WHERE
                    query = query.rstrip(", ") + " WHERE id_frais_supplementaires = %s"
                    values.append(id_frais_supplementaires)

                    # Execution 
                    cursor.execute(query, tuple(values))
                    connection.commit()
                    # Retour
                    return True
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return False
        
    def delete_frais_supplementaires(self, id_frais_supplementaires):
        """Supprime un frais supplémentaire par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "DELETE FROM frais_supplementaires WHERE id_frais_supplementaires = %s"
                    # Parametres
                    value = (id_frais_supplementaires,)
                    # Execution 
                    cursor.execute(query, value)
                    connection.commit()
                    # Retour
                    return True
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return False