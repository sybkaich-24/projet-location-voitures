import mysql.connector
from mysql.connector import Error

class ClientDAO:
    def __init__(self, host, user, password, database):
        self.config = {
            'host': host,
            'user': user,
            'password': password,
            'database': database,
            'port': 3307 
        }

    def get_client_by_id(self, id_client):
        """Récupère un client par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT * FROM client WHERE id_client = %s"
                    # Parametres
                    value = (id_client,)
                    # Execution 
                    cursor.execute(query, value)
                    # Resultat
                    result = cursor.fetchone()
                    # Retour
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_id_client_by_email(self, email):
        """Récupère l'ID d'un client par son email"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT id_client FROM client WHERE email = %s"
                    # Parametres
                    value = (email,)
                    # Execution 
                    cursor.execute(query, value)
                    # Resultat
                    result = cursor.fetchone()
                    # Retour
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_id_client_by_numero_permis(self, numero_permis):
        """Récupère l'ID d'un client par son numéro de permis"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT id_client FROM client WHERE numero_permis = %s"
                    # Parametres
                    value = (numero_permis,)
                    # Execution 
                    cursor.execute(query, value)
                    # Resultat
                    result = cursor.fetchone()
                    # Retour
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None

    def get_all_clients(self):
        """Récupère tous les clients"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT * FROM client"
                    # Execution 
                    cursor.execute(query)
                    # Resultat
                    result = cursor.fetchall()
                    # Retour
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def create_client(self, nom, prenom, email, telephone, numero_permis):
        """Crée un nouveau client"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "INSERT INTO client (nom, prenom, email, telephone, numero_permis, date_inscription) VALUES (%s, %s, %s, %s, %s, NOW())"
                    # Parametres
                    values = (nom, prenom, email, telephone, numero_permis)
                    # Execution 
                    cursor.execute(query, values)
                    # Commit des changements
                    connection.commit()
                    # Retour 
                    return True
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return False
        
        def update_client(self, id_client, nom=None, prenom=None, email=None, telephone=None, numero_permis=None):
            """Met à jour un client"""

            try:
                with mysql.connector.connect(**self.config) as connection:
                    with connection.cursor() as cursor:
                        # Construction de la requete de mise à jour avec les champs à mettre à jour
                        query = "UPDATE client SET "
                        values = []
                        if nom is not None:
                            query += "nom = %s, "
                            values.append(nom)
                        if prenom is not None:
                            query += "prenom = %s, "
                            values.append(prenom)
                        if email is not None:
                            query += "email = %s, "
                            values.append(email)
                        if telephone is not None:
                            query += "telephone = %s, "
                            values.append(telephone)
                        if numero_permis is not None:
                            query += "numero_permis = %s, "
                            values.append(numero_permis)
                        # Retirer la virgule finale et ajouter la clause WHERE
                        query = query.rstrip(", ") + " WHERE id_client = %s"
                        values.append(id_client)
                        # Execution de la requete avec les parametres
                        cursor.execute(query, tuple(values))
                        # Commit des changements
                        connection.commit()
                        # Retour 
                        return True
            except Error as e:
                print(f"Error while connecting to MySQL: {e}")
                return False
            
    def desinscription_client_by_id(self, id_client):
        """Désinscrit un client en le rendant anonyme et en changant sa date de désinscription"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "UPDATE client SET nom = 'Anonyme', prenom = 'Anonyme', email = NULL, telephone = NULL, numero_permis = NULL, date_desinscription = NOW() WHERE id_client = %s"
                    # Parametres
                    value = (id_client,)
                    # Execution 
                    cursor.execute(query, value)
                    # Commit des changements
                    connection.commit()
                    # Retour 
                    return True
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return False
            
    def delete_client(self, id_client):
        """Supprime un client par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "DELETE FROM client WHERE id_client = %s"
                    # Parametres
                    value = (id_client,)
                    # Execution 
                    cursor.execute(query, value)
                    # Commit des changements
                    connection.commit()
                    # Retour 
                    return True
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return False