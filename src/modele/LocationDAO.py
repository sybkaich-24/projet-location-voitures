import mysql.connector
from mysql.connector import Error

class LocationDAO:
    def __init__(self, host, user, password, database):
        self.config = {
            'host': host,
            'user': user,
            'password': password,
            'database': database,
            'port': 3307 # Il faut s'assurer que le port de docker est le meme 
        }
        
    def get_location_by_id(self, id_location):
        """Récupère une location par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT * FROM location WHERE id_location = %s"
                    # Parametres
                    value = (id_location,)
                    # Execution 
                    cursor.execute(query, value)
                    # Resultat
                    result = cursor.fetchone()
                    # Retour
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_all_locations(self):
        """Récupère toutes les locations"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT * FROM location"
                    # Execution 
                    cursor.execute(query)
                    # Resultat
                    result = cursor.fetchall()
                    # Retour
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
    
    def get_id_location_by_id_reservation(self, id_reservation):
        """Récupère l'ID d'une location par son ID de réservation"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT id_location FROM location WHERE id_reservation = %s"
                    # Parametres
                    value = (id_reservation,)
                    # Execution 
                    cursor.execute(query, value)
                    # Resultat
                    result = cursor.fetchone()
                    # Retour
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_all_locations_by_id_vehicule(self, id_vehicule):
        """Récupère toutes les locations d'un véhicule par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT * FROM location WHERE id_vehicule = %s"
                    # Parametres
                    value = (id_vehicule,)
                    # Execution 
                    cursor.execute(query, value)
                    # Resultat
                    result = cursor.fetchall()
                    # Retour
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_all_locations_by_id_client(self, id_client):
        """Récupère toutes les locations d'un client par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT * FROM location WHERE id_client = %s"
                    # Parametres
                    value = (id_client,)
                    # Execution 
                    cursor.execute(query, value)
                    # Resultat
                    result = cursor.fetchall()
                    # Retour
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_all_locations_by_id_agence_depart(self, id_agence_depart):
        """Récupère toutes les locations d'une agence de départ par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT * FROM location WHERE id_agence_depart = %s"
                    # Parametres
                    value = (id_agence_depart,)
                    # Execution 
                    cursor.execute(query, value)
                    # Resultat
                    result = cursor.fetchall()
                    # Retour
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_all_locations_by_id_agence_retour(self, id_agence_retour):
        """Récupère toutes les locations d'une agence de retour par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT * FROM location WHERE id_agence_retour = %s"
                    # Parametres
                    value = (id_agence_retour,)
                    # Execution 
                    cursor.execute(query, value)
                    # Resultat
                    result = cursor.fetchall()
                    # Retour
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def create_location(self, date_debut, date_fin_prevue, date_retour_reelle, prix_total, statut_location, kilometrage_depart, kilometrage_retour, id_client, id_vehicule, id_reservation, id_agence_depart, id_agence_retour):
        """Crée une nouvelle location"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "INSERT INTO location (date_debut, date_fin_prevue, date_retour_reelle, prix_total, statut_location, kilometrage_depart, kilometrage_retour, id_client, id_vehicule, id_reservation, id_agence_depart, id_agence_retour) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    # Parametres
                    value = (date_debut, date_fin_prevue, date_retour_reelle, prix_total, statut_location, kilometrage_depart, kilometrage_retour, id_client, id_vehicule, id_reservation, id_agence_depart, id_agence_retour)
                    # Execution 
                    cursor.execute(query, value)
                    # Commit pour sauvegarder les changements
                    connection.commit()
                    # Retour
                    return True
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return False
    
    def update_location(self, id_location, date_debut=None, date_fin_prevue=None, date_retour_reelle=None, prix_total=None, statut_location=None, kilometrage_depart=None, kilometrage_retour=None, id_client=None, id_vehicule=None, id_reservation=None, id_agence_depart=None, id_agence_retour=None):
        """Met à jour une location"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Construction de la requête de mise à jour
                    query = "UPDATE location SET "
                    values = []
                    
                    if date_debut is not None:
                        query += "date_debut = %s, "
                        values.append(date_debut)
                    if date_fin_prevue is not None:
                        query += "date_fin_prevue = %s, "
                        values.append(date_fin_prevue)
                    if date_retour_reelle is not None:
                        query += "date_retour_reelle = %s, "
                        values.append(date_retour_reelle)
                    if prix_total is not None:
                        query += "prix_total = %s, "
                        values.append(prix_total)
                    if statut_location is not None:
                        query += "statut_location = %s, "
                        values.append(statut_location)
                    if kilometrage_depart is not None:
                        query += "kilometrage_depart = %s, "
                        values.append(kilometrage_depart)
                    if kilometrage_retour is not None:
                        query += "kilometrage_retour = %s, "
                        values.append(kilometrage_retour)
                    if id_client is not None:
                        query += "id_client = %s, "
                        values.append(id_client)
                    if id_vehicule is not None:
                        query += "id_vehicule = %s, "
                        values.append(id_vehicule)
                    if id_reservation is not None:
                        query += "id_reservation = %s, "
                        values.append(id_reservation)
                    if id_agence_depart is not None:
                        query += "id_agence_depart = %s, "
                        values.append(id_agence_depart)
                    if id_agence_retour is not None:
                        query += "id_agence_retour = %s, "
                        values.append(id_agence_retour)

                    # Retirer la dernière virgule et ajouter la clause WHERE
                    query = query.rstrip(", ") + " WHERE id_location = %s"
                    values.append(id_location)

                    # Execution 
                    cursor.execute(query, tuple(values))
                    # Commit pour sauvegarder les changements
                    connection.commit()
                    # Retour
                    return True
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return False
        
    def delete_location(self, id_location):
        """Supprime une location par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "DELETE FROM location WHERE id_location = %s"
                    # Parametres
                    value = (id_location,)
                    # Execution 
                    cursor.execute(query, value)
                    # Commit pour sauvegarder les changements
                    connection.commit()
                    # Retour
                    return True
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return False
