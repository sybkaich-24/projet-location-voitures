from vue.interface import VueTerminal
from modele.AgenceDAO import AgenceDAO
from modele.Agent_d_agenceDAO import Agent_d_agenceDAO
from modele.CategorieVehiculeDAO import CategorieVehiculeDAO
from modele.ClientDAO import ClientDAO
from modele.ComptableDAO import ComptableDAO
from modele.EmployeDAO import EmployeDAO
from modele.FraisSupplementaireDAO import FraisSupplementaireDAO
from modele.LocationDAO import LocationDAO
from modele.PaiementDAO import PaiementDAO
from modele.VueDAO import VueDAO
from modele.ReservationDAO import ReservationDAO
from modele.VehiculeDAO import VehiculeDAO

from datetime import date
from decimal import Decimal

class Application:
    def __init__(self):
        self.vue = VueTerminal()
        self.agence_dao = AgenceDAO(host='localhost', user='root', password='root123', database='location_voitures', port=3307)
        self.agent_d_agence_dao = Agent_d_agenceDAO(host='localhost', user='root', password='root123', database='location_voitures', port=3307)
        self.categorie_vehicule_dao = CategorieVehiculeDAO(host='localhost', user='root', password='root123', database='location_voitures', port=3307)
        self.client_dao = ClientDAO(host='localhost', user='root', password='root123', database='location_voitures', port=3307)
        self.comptable_dao = ComptableDAO(host='localhost', user='root', password='root123', database='location_voitures', port=3307)
        self.employe_dao = EmployeDAO(host='localhost', user='root', password='root123', database='location_voitures', port=3307)
        self.frais_supplementaire_dao = FraisSupplementaireDAO(host='localhost', user='root', password='root123', database='location_voitures', port=3307)
        self.location_dao = LocationDAO(host='localhost', user='root', password='root123', database='location_voitures', port=3307)
        self.paiement_dao = PaiementDAO(host='localhost', user='root', password='root123', database='location_voitures', port=3307)
        self.vue_dao = VueDAO(host='localhost', user='root', password='root123', database='location_voitures', port=3307)
        self.reservation_dao = ReservationDAO(host='localhost', user='root', password='root123', database='location_voitures', port=3307)
        self.vehicule_dao = VehiculeDAO(host='localhost', user='root', password='root123', database='location_voitures', port=3307)

    def run(self):
        """Est appeler en premier pour demarer l'app, celle ci appele la methode adequate de la vue pour afficher la page d'acceuil"""

        self.vue.display_welcome_message()
        while True:
            """
            Les differents coix possibles sont:
            0: Quitter l'application
            1: Inscription
            2: Informations personnelles
            3: Modifier les informations personnelles
            4: Désinscription
            5: Louer une voiture
            6: Rapport annuel des ventes
            """
            choise = self.vue.display_main_menu()
            
            match choise:
                case '0':
                    # Quitter l'application
                    self.vue.display_goodbye_message()
                    break
                case '1': 
                    # Inscription
                    client_data = self.vue.sing_up_client()
                    self.client_dao.create_client(**client_data)
                case '2':
                    # Informations personnelles
                    email = self.vue.get_email_client()
                    id_client = self.client_dao.get_id_client_by_email(email)
                    client_info = self.client_dao.get_client_by_id(id_client)
                    self.vue.display_client_info(client_info)
                case '3':
                    # Modifier les informations personnelles
                    client_data = self.vue.sing_up_client()
                    self.client_dao.update_client(**client_data)
                case '4':
                    # Désinscription
                    email = self.vue.get_email_client()
                    id_client = self.client_dao.get_id_client_by_email(email)
                    self.client_dao.desinscription_client_by_id(id_client)
                case '5':
                    # Louer une voiture
                    """
                    Une location s'effectue comme suit:
                    1. le client entre son email pour verifier son identté et récupérer son ID 
                    2. le client choisit une voiture à louer parmi les voitures disponibles (pour chaque voiture on affiche toutes ses caractéristiques)
                    3. le client choisit une voiture et une date de debut et de fin de location
                    4. le client choisit le moyen de payement et procède au paiement
                    5. le client reçoit une confirmation de sa location
                    """
                    email = self.vue.get_email_client()
                    id_client = self.client_dao.get_id_client_by_email(email)
                    # Affichage des voitures disponibles (uniquement)
                    vehicules_disponibles = self.vue_dao.get_vehicules_disponibles()
                    id_vehicule = self.vue.display_available_cars_menu(vehicules_disponibles)
                    # Récupération des dates de début et de fin de location
                    date_debut, date_fin = self.vue.get_rental_dates()
                    # Calcule du nombre de jours
                    nb_jours = days_between(date_debut, date_fin)
                    # Prix total de la location

                    tarif_row = self.vehicule_dao.get_tarif_journalier_vehicule_by_id(id_vehicule)
                    if isinstance(tarif_row, dict):
                        tarif_value = tarif_row.get("tarif_journalier")
                    elif isinstance(tarif_row, (tuple, list)) and len(tarif_row) > 0:
                        tarif_value = tarif_row[0]
                    else:
                        tarif_value = None

                    if tarif_value is None:
                        self.vue.display_invalid_option_message()
                        continue

                    if isinstance(tarif_value, (int, float, Decimal, str, bytes)):
                        prix_journalier = float(tarif_value)
                    else:
                        self.vue.display_invalid_option_message()
                        continue
                    
                    prix_total = nb_jours * prix_journalier
                    # Récupération du moyen de paiement et le montant choisi
                    moyen_paiement, montant = self.vue.get_payment_infos()
                    # Création de la location
                    kilometrage_depart = self.vehicule_dao.get_kilometrage_actuel_vehicule_by_id(id_vehicule)
                    id_agence_depart = self.vehicule_dao.get_id_agence_vehicule_by_id(id_vehicule)
                    id_agence_retour = id_agence_depart
                    id_categorie = self.vehicule_dao.get_id_categorie_vehicule_by_id(id_vehicule)
                    # Création de la reservation
                    id_reservation = self.reservation_dao.create_reservation(date_debut, date_fin, 'en cours', id_client, id_vehicule, id_categorie )
                    id_location = self.location_dao.create_location(date_debut, date_fin, prix_total, 'en cours', kilometrage_depart, None, id_client, id_vehicule, id_reservation, id_agence_depart, id_agence_retour)
                    # Comfirmation
                    self.vue.display_rental_confirmation(id_location)
                case '6':
                    # Rapport annuel des ventes
                    """
                    L'obtention d'un rapport s'effectue comme suit:
                    1. le comptable entre son email pour verifier son identté et récupérer son ID
                    2. le comptable choisit l'année pour laquelle il veut obtenir le rapport annuel
                    3. le comptable reçoit le rapport annuel des ventes de l'année choisie
                    """
                    email = self.vue.get_email_member_comptabilite()
                    id_employe = self.employe_dao.get_id_employe_by_email(email)
                    comptable = self.comptable_dao.get_comptable_by_id(id_employe)
                    if self.vue.is_comptabilite_member_valid(comptable):
                        year = self.vue.get_year_for_sales_report()
                        report_mensuel = self.vue_dao.get_chiffre_affaires_mensuel_by_annee(year)
                        report_annuel = self.vue_dao.get_chiffre_affaires_annuel(year)
                        self.vue.display_sales_report(report_mensuel, report_annuel, year)

                case _:
                    self.vue.display_invalid_option_message()

def days_between(date1, date2):
    """Calcule le nombre de jours entre deux dates"""
    d1 = date(date1[0], date1[1], date1[2])
    d2 = date(date2[0], date2[1], date2[2])
    return abs((d2 - d1).days)