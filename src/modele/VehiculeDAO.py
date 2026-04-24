import mysql.connector
from mysql.connector import Error

class VehiculeDAO:
    def __init__(self, host, user, password, database):
        self.config = {
            'host': host,
            'user': user,
            'password': password,
            'database': database,
            'port': 3307 # Il faut s'assurer que le port de docker est le meme 
        }
