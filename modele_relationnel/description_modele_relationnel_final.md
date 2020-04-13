# Description du modèle relationnel final

## Les tables
* [accidents_events](#accidents_events)
* [flight_info](#flight_info)
* [fatalities_reports](#fatalities_reports)
* [aircrafts](#aircrafts)
* [airports](#airports)
* [departure_airport](#departure_airport)
* [destination_airport](#destination_airpot)
Un schéma des tables est dispoonible sous format png ([modele_final.png](https://github.com/elvinaeury/Projet_SBD/blob/master/modele_relationnel/modele_final.png)) ou sous format pdf ([modele_final.pdf](https://github.com/elvinaeury/Projet_SBD/blob/master/modele_relationnel/modele_final.pdf)). Le script [script_modele_final.sql](https://github.com/elvinaeury/Projet_SBD/blob/master/modele_relationnel/script_modele_final.sql) peut créer ces tables pour un chargement déstiné au SGBDR postgres

## accidents_events
Décrit l'accident :
* *id_event*: clé primaire (autogénérée et autoincrementée : type SERIAL). Il faudra peut-être passer à BIGSERIAL en fonction du volume de donées
* *day* : le jour de la semaine où l'accident a eu lieu ; peut être intéressant pour certaines requêtes (par exemple vérifier si les accidents se répartissent uniformément sur les 7 jours de la semaine : loi uniforme sur {1,...,7})
* *date* : En cas d'enregistrement sous un type timestamp, ce champ donne la date et l'heure de l'accident (même intérêt que day). Autrement, il sera peut-être enregistré sous type varchar en fonction des données. Exemple de requête : vérifier les accidents surviennent plus pendant les heures nocturnes ou diurnes.
* *type_event* : Valeurs possibles : A1,B1,C2, etc... d'où type varchar(2). Elle permet de distinguer accident, incident, sabotage etc et permettrait diverifier les requêtes et obtenir des résultats pertinents facilement interprétables.
* *phase* : phase de vol de l'appareil lors de l'accident (voir si on peut identifier toutes les valeurs possibles car le site donné en référence danns le document d'aviation safaty est inaccessible).
* *location* : le lieu de l'accident ou le lieu proche (d'après les données). Peut être un océan en cas d'accident dans les eaux internationales
* *country* : nom du pays où a eu lieu l'accident. Peut être aussi un océan. A récupérer dans la colonne location des données, sera utile pour des requêtes sur des pays 
* *total_occupants* : nombre total des personnes à bord de l'avion
* *total_fatalities* : nombre total des victimes (y compris celles n'ayant pas été à bord de l'appareil)
* *aircraft_damage* : dommages sur l'appareil (voir valeurs possibles dans la description des données). Valeur remarquée par exemple : destroyed mais qui n'apparaît pas dans la description
* *aircraft_fate* : mêmes valeurs que aircraft_damage d'après la description des données (mais la description est faite plus pour ce champ on dirait)

## flight_info
Donne les informations sur le vol concerné par l'accident :
* *id_flight* : clé primaire de type SERIAL (même remarque que pour la primary key précédente)
* *operator* : operateur lors du vol (contiendra soit les infos de la colonne operator des données si existantes, soit celles de la colonne leased from sinon)
* *nature* : militaire, domestique, internationale, etc
* *flight_number* : numéro de vol donné par la compagnie (je ne crois pas qu'on servira beaucoup de cette info dans la suite mais on la garde pour l'instant)
* *crew_number* : nombre de membres d'équipage (nom renseigné quelquefois dans les données pour certaines années 19..)
* *passengers_number* : nombre de passagers (pareil)

## fatalities_reports
Donne le bilan sur les victimes  :
* *id_report* : clé primaire (mêmes remarques que pour les clés précédentes)
* *crew_fatalities* : nombre de victimes parmi les membres d'équipage 
* *passengers_fatalities* : nombre de victimes parmi les passagers
* *collision_casualties* : nombre de victimes à bord des autres appareils en cas d'une potentielle collision
* *ground_casualties* :nombre de victime au sol
* *status* : champ de type varchar spécifiant si les infos sont officielles, ... et qui peut-être intéressant pour certaines requêtes. (Voir les valeurs possibles dans le document de desciption de données)

## aircrafts
Donne les informations sur l'appareil accidenté (en dehors des dommages subis) : 
* *id_aircraft* : clé primaire (mêmes remarques que précédemment)
* *type_aircraft* : modèle de l'appareil
* *year_built* : année de construction (ce champ a été supprimé et ne compte donc pas)
* *number_engines* : nombre de moteurs
* *type_engines* : type moteur (on n'en aura peut-être pas besoin pour la suite mais qui sait)
*  *first_flight* : année du premier vol
*  *cycles* : nombre de cycles "décollage - atterrissage" 
*  *total_airframe_hours* : nombre d'heures cumulées de tous les vols 
*  *registration* : enregistrement de l'appareil
*  *c_n_msn* :numéro de série de l'appareil (pas toujours connu sinon il aurait permis d'identifier un appareil une et une seule fois)

## airports
Recense tous les aéroports récupérés à partir du fichier airports.dat.txt et ceux qui ne s'y trouvent pas mais qui interviennent dans les données venant du site aviation safety :
* *code_icao* : code à 4 lettres permettant de distinguer un aéroport de façon unique
* *code_iata* : code à 3 lettres (pas toujours renseigné dans les données issues du fichier airports.dat.txt)
* *name* : nom de l'aéroport
* *city* : ville où il se situe (lorsque c'est renseigné)
* *country* : pays (toujours renseigné)
* *latitude*
* *longitiude*
* *altitude*
Ces trois derniers champs ne sont pas renseignés dans les données issues de aviation safety

## departure_airport
Etablit le lien entre l'aéroport de départ (dans la table [airports](#airports)) et le vol concerné (dans la table [flight_info](#flight_info)) :
* *flight* : clé étrangère référençant la table [flight_info](#flight_info)
* *icao* : clé étrangère référençant la table [airports](#airports)

## destination_airport
Etablit le lien entre l'aéroport de destination (dans la table [airports](#airports)) et le vol concerné (dans la table [flight_info](#flight_info)) :
* *flight* : clé étrangère référençant la table [flight_info](#flight_info)
* *icao* : clé étrangère référençant la table [airports](#airports)

## Quid du traitement des données manquantes pour la suite ?
Nous ne supprimerons pas les données manquantes car elles sont hétérogènes et donc nous perdrions la plupart des colonnes qui sont intéressantes pour nos futures reqêtes et analyses. Lors du nettoyage des données, nous affecterons la chaîne "-" aux champs non renseignés. Ainsi lors du peuplement des tables, tout champ avec cette chaîne sera enregistré comme champ NULL. Cela supposera ne pas avoir mis de contrainte de non nullité lors de la création des classes dans django.
Quelques difficultés envisageables : 
 * le champ date ne poura pas être de type timestamp car cela nécessite au moins la connaissance de l'année, du mois et du jour. Il sera donc enregistré sous forme de chaîne de caractères, ce qui poura peut-être compliqué certains de nos futurs traitements
 * une solution sera pêut-être de supprimer les enregistrements pour lesquels la date exacte n'est pas connue (si ils ne sont pas très nombreux) ou bien créer une table particulière qui pourra les contenir (à voir tout au long de l'évolution du projet et des besoins qui en découleront)
