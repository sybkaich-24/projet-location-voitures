# Détail de la logique de base du back end
## Architecture
- La ethode de comunication avec la base de donnée choisie est une application console
- Cette derniere est implementée suivant le modele MVC (modele vue controleur)     
1) Le dossier modele contient l'ensemble des entiter de la tables, ainsi que l'ensemble des fonction/methode permettant d'interagir avec la base de donnée (DAO)
2) Le dossier vue contient l'ensemble de la logique relatif a l'interaction avec l'utilisateur ce package contient donc les fonction/methode permettant de recolter les donnée entrée par l'utilisateur et d'afficher les resultat
3) Ce dernier dossier contient le package servant de communication entre les differents modeles et la vue, il se chargera de transmettre les information envoyer par la vue au modeles correspondant apres verification, et de renvoyer la reponse a la vue apres reception de la reponse coter modele