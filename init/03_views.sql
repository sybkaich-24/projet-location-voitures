USE location_voitures;

CREATE OR REPLACE VIEW VueVehiculesDisponibles AS
SELECT
    V.id_vehicule,
    V.immatriculation,
    V.marque,
    V.modele,
    V.annee,
    V.kilometrage_actuel,
    V.etat_vehicule,
    V.tarif_journalier,
    C.nom_categorie,
    A.nom_agence,
    A.ville
FROM Vehicule V, CategorieVehicule C, Agence A
WHERE V.id_categorie = C.id_categorie
  AND V.id_agence = A.id_agence AND V.etat_vehicule = 'disponible';

CREATE OR REPLACE VIEW VueChiffreAffairesMensuel AS
SELECT
    YEAR(P.date_paiement) AS annee,
    MONTH(P.date_paiement) AS mois,
    SUM(P.montant) AS chiffre_affaires_mensuel
FROM Paiement P WHERE 
    P.statut_paiement = 'effectue'
GROUP BY YEAR(P.date_paiement), MONTH(P.date_paiement);

CREATE OR REPLACE VIEW VueRapportAnnuel AS
SELECT
    YEAR(P.date_paiement) AS annee,
    SUM(P.montant) AS chiffre_affaires_annuel
FROM Paiement P WHERE P.statut_paiement = 'effectue'
GROUP BY YEAR(P.date_paiement);