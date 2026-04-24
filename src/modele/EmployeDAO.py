import mysql.connector
from mysql.connector import Error

class EmployeDAO:
    def __init__(self, host, user, password, database):
        self.config = {
            'host': host,
            'user': user,
            'password': password,
            'database': database,
            'port': 3307 # Il faut s'assurer que le port de docker est le meme 
        }

    def get_employe_by_id(self, id_employe):
        """Récupère un employé par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT * FROM employe WHERE id_employe = %s"
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
        
    def get_id_employe_by_email(self, email):
        """Récupère l'ID d'un employé par son email"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT id_employe FROM employe WHERE email = %s"
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
        
    def get_all_employes(self):
        """Récupère tous les employés"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT * FROM employe"
                    # Execution 
                    cursor.execute(query)
                    # Resultat
                    result = cursor.fetchall()
                    # Retour
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def create_employe(self, nom, prenom, email, telephone, date_embauche, id_agence):
        """Crée un nouvel employé"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "INSERT INTO employe (nom, prenom, email, telephone, date_embauche, id_agence) VALUES (%s, %s, %s, %s, %s, %s)"
                    # Parametres
                    values = (nom, prenom, email, telephone, date_embauche, id_agence)
                    # Execution 
                    cursor.execute(query, values)
                    # Validation de la transaction pour rendre definitif les modifications
                    connection.commit()
                    # Retour
                    return True
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return False
        
    def update_employe(self, id_employe, nom=None, prenom=None, email=None, telephone=None, date_embauche=None, id_agence=None):
        """Met à jour les informations d'un employé"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Construction de la requete de mise à jour dynamique en fonction des paramètres fournis
                    query = "UPDATE employe SET "
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
                    if date_embauche is not None:
                        query += "date_embauche = %s, "
                        values.append(date_embauche)
                    if id_agence is not None:
                        query += "id_agence = %s, "
                        values.append(id_agence)
                    
                    # Retirer la dernière virgule et ajouter la clause WHERE
                    query = query.rstrip(", ") + " WHERE id_employe = %s"
                    values.append(id_employe)

                    # Execution de la requete avec les parametres
                    cursor.execute(query, tuple(values))
                    # Validation de la transaction pour rendre definitif les modifications
                    connection.commit()
                    # Retour du resultat
                    return True
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return False
        
    def delete_employe(self, id_employe):
        """Supprime un employé par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "DELETE FROM employe WHERE id_employe = %s"
                    # Parametres
                    value = (id_employe,)
                    # Execution 
                    cursor.execute(query, value)
                    # Validation de la transaction pour rendre definitif les modifications
                    connection.commit()
                    # Retour
                    return True
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return False