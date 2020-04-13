# PROJET_SGBD

Bienvenue sur ce dépôt git consacré au projet universitaire de notre cours de [bases de données relationnelles](https://math.univ-angers.fr/~ducrot/bddr/) du Master 1 Data Science de l'Université d'Angers. 

Ce projet est réalisé par : 
* [Destin ASHUZA CIRUMANGA](https://github.com/dest-ash)
* [Nadia GHERNAOUT](https://github.com/nadatum)
* [Elvina GOVENDASAMY](https://github.com/elvinaeury)

## Table of contents
* [Cahier des charges](#cahier-des-charges)
* [Sujet d'étude](#sujet-d-etude)
* [Progression du travail](#progression-du-travail)
* [TO-DO list](#to-do-list)

## Cachier des charges
L'énoncé précis du projet, son contexte de réalisation ainsi que les différentes contraintes à respecter sont définis de manière détaillée sur le [site de la formation](https://math.univ-angers.fr/~jaclin/2020ds1/evalDS1bdd/2020/2020/2020.html). 

Dans cette section, nous en faisons juste un bref récapitulatif.

### Données mises à disposition
Différentes sources de donées  liés au traffic aérien :
https://www.data.gouv.fr/en/datasets/donnees-despace-aerien-de-la-base-aeronautique-du-sia/ ,
https://openflights.org/data.html ,
https://aviation-safety.net/database/ , 
https://www.ntsb.gov/_layouts/ntsb.aviation/index.aspx ,
https://www.transtats.bts.gov/databases.asp?Mode_ID=1&Mode_Desc=Aviation&Subject_ID2=0

### Objectif
Définir un sujet d'études à partir de ces données et réaliser une application web qui servira d'interface utilisateur à tout internaute souhaitant intéragir avec les données en fonction du sujet retenu

### A réaliser 
* Concevoir et peupler une base de données multi-tables sous formes normales
* Concevoir l'application web

### Contraintes 
Utilisation du SGBD postegreSQL et du framework Django, consignation en temps réel de l'avancement du travail sur github.

## Sujet d'étude 
Nous avons retenu comme sujet l'étude des **Incidents d'avions à travers le monde.**
Concrétement, nous allons concevoir une base de données et une application permettant de l'interroger aux travers des requêtes telles ques :
- Quels sont les endroits où il y a le plus d’accidents/ incidents (entre certaines dates)
- Afficher les types d'accidents ou incidents ayant fait le plus de blessés/morts
- Donner un aéroport de départ et les incidents qui qui se sont passés et leur distance par rapport à cet aéroport (si possible) et des caractéristiques sur ces accidents 
- Combien d'accidents par année ? (puis graphique)
- liste des accidents :
  - par année
  - par type d'avion
  - par localisation
- Pendant quelle phase de vol est survenu l'incident : landing ? take-off ? during flight ?
- Et toute autre requête qui sera possible à partir des données disponibles

Les résultats seront rendus sous un format de visualisation adéquat et agréable.

## Etat d'avancement du projet

### Données :
Toutes les données nécessaires au projet ont été récupérées, nettoyées et mises sous une forme exploitable.

Les données brutes sont décrites dans le fichier [donnees.md](https://github.com/elvinaeury/Projet_SBD/blob/master/donnees/donnees.md) (accessible au clic) et se retrouvent dans le répertoire [donnees](https://github.com/elvinaeury/Projet_SBD/tree/master/donnees). Elles ont été récupérées en partie par [web_scraping](https://github.com/elvinaeury/Projet_SBD/tree/master/web_scraping) et la procédure est décrite via le fichier [web_scraping.md](https://github.com/elvinaeury/Projet_SBD/blob/master/web_scraping/web_scraping.md)

Quant aux données traitées, elles se retrouvent dans le dossier [nettoyage](https://github.com/elvinaeury/Projet_SBD/tree/master/nettoyage) dont la description est faite dans [nettoya.md](https://github.com/elvinaeury/Projet_SBD/blob/master/nettoyage/nettoyage.md)

### Description des fichiers
Comme pour les données, tous les fichiers de ce dépôt sont  répartis dans des différents dossiers et chaque dossier contient un fichier **.md** qui décrit son contenu. En cliquant sur le nom d'un dossier ou d'un fichier mentionné sur cette page, vous accédez directement à la ressource concernée.

Les programmes réalisés et les fonctionalités à venir seront décrits de la même manière.

### Etat de la base des données
Le modèle des données conçu sous postgreSQL et décrit dans le fichier [modele_relationnel/descriptif_modele_relationnel_final.md](https://github.com/elvinaeury/Projet_SBD/blob/master/modele_relationnel/description_modele_relationnel_final.md) a été réalisé et peuplé avec succès via [Django](https://github.com/elvinaeury/Projet_SBD/tree/master/Django) et les détails sont à retrouver dans le fichier [description_dossier_django.md](https://github.com/elvinaeury/Projet_SBD/blob/master/Django/description_dossier_django.md)

## TO-DO List

- [x] Choisir toutes les données et les récuperer
- [x] Remplir le GitHub public avec plus de renseignements pour les profs
- [x] Créer un [modèle relationnel](https://github.com/elvinaeury/Projet_SBD/tree/master/modele_relationnel)
- [x] Se renseigner sur le web scrapping (avec module `beautiful-soup`)
- [x] [Web Scrapping](https://github.com/elvinaeury/projet_test/blob/master/Web_scrapping/web.md)
- [x] Nettoyer les données récupérées
- [x] Création du projet django[DjangoAviation](https://github.com/elvinaeury/Projet_SBD/tree/master/Django/DjangoAviation), de l'application [appliweb](https://github.com/elvinaeury/Projet_SBD/tree/master/Django/DjangoAviation/appliweb) et peuplement de la base de données.
- [ ] Jouer les scripts django et de peuplement sur le serveur de l'université également
- [ ] Commencer la partie framework
- [ ] Créer les vues et templates correspondant aux requêtes envisagées
- [ ] Etudier l'aspect visualisation et présentation des requêtes (css, html, graphiques, imagages, etc)
- [ ] Tester l'utlisation du timestamp pour les champs date et time
- [ ] Finaliser l'application et régler les derniers points.
- [ ] Bonus : Faire de l'analyse des données (datamining) et des stats si le temps et les donnees le permettent et créer des vues correspondantes