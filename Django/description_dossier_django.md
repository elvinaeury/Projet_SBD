# Description du dossier Django

Ce dossier contient tous les fichiers relatifs à l'utilisation de django dans le cadre de ce projet (parties ORM et framework)

* Environnement du projet django  : [*DjangoAviation*](https://github.com/elvinaeury/Projet_SBD/tree/master/Django/DjangoAviation)
* Nom de l'application qui servira d'interface utilisateur : [*appliweb*](https://github.com/elvinaeury/Projet_SBD/tree/master/Django/DjangoAviation/appliweb)

## Partie ORM
 
### Utilisation du SGBD postgres
Le paramétrage du projet a été fait et l'utilisation du SGBD actée (voir le fichier [DjangoAviation/settings.py](https://github.com/elvinaeury/Projet_SBD/blob/master/Django/DjangoAviation/DjangoAviation/settings.py))

### Création et ajustement du modèle de données pour Django
Le modèle relationnel tel que décrit dans  [modele_relationnel/description_du_modele_relationne_final.md](https://github.com/elvinaeury/Projet_SBD/blob/master/modele_relationnel/description_modele_relationnel_final.md) est donc matérialisé ici via les classes django définies dans le fichier [appliweb/models.py](https://github.com/elvinaeury/Projet_SBD/blob/master/Django/DjangoAviation/appliweb/models.py)
Comme pressenti auparavant, les données manquantes ont engendré certaines contraintes comme la duplication du champ date d'un type timestamp en deux champs date et time de type varchar. Comme déjà mentionné, en fonction des futurs besoins, il sera peut-être question de supprimer ces données manquantes pour utiliser le bon type ou de les mettre dans une table à part. Il n'en est pas encore question à ce stade.

### Chargement des données dans les tables ainsi créées 
Le peuplement de la base se fait en deux étapes :
- peuplement de la table airports : se fait avec [script_peuplement_airports2.py](https://github.com/elvinaeury/Projet_SBD/blob/master/Django/script_peuplement_aiports2.py)
- peuplement des autres tables : se fait avec [scrip_peuplement_incidents2.py](https://github.com/elvinaeury/Projet_SBD/blob/master/Django/script_peuplement_incidents2.py)
Les scripts ont été testés avec succès et le chargement des données sera fait bientôt sur le serveur postgres de l'université.


## Partie FrameWork 

Les prochaines étapes seront consancrées à la partie web de l'application qui fera office d'interface utilisateur. Les différentes évolutions seront consignées ici progressivement.

### Les vues

Différentes vues ont été créées pour les pages de l'application.  Elles sont réparties dans les fichiers `views.py` et `views2.py` de l'application Django. Leur liaison au contrôleur a été faite via les urls de l'application disponibles dans le fichier `urls.py`

Ces vues utilisent le formalisme Django pour parcourir, interroger et croiser les différentes tables de la base de données.

### Les templates

Le rendu produit par nos vues est optimisé grâce aux différents templates qui se trouvent dans le dossier `template` de l'application. Ces templates utlisent aussi certaines images qui se retrouvent dans le dossier `static` de l'application.

### Les fonctionnalités disponibles 

L'application réalisée offre quelques fonctionnalités pour parcourir les données.

Dès la page d'accueil, l'utilisateur a accès à certaines informations et statistiques fournies par les vues et issues du croisement de différentes tables de notre base de données.

En plus de cela, il a aussi la possibilité de parcourir certaines tables comme la table enregistrant les aéroports. IL a peut aussi parcourir la table des accidents soit globalement, soit en la filtrant suivant une année précise, consulter les accidents survenus à une date précise de son choix ou afficher tous les accidents survenus entre deux dates exactes qu'il aura choisies. 

Ces possibilités de recherche ont été implentées grâce aux formulaires Django. Les résultats sont rendus sur plusieurs pages suivant le nombre d'enregistrements statisfaisant la requête lancée, ce qui permet un chargement rapide des pages. Cette pagination a été faite grâce au module `Paginator` de Django.

En utlilisant les mêmes techniques, il est possible de coder toutes les requêtes que l'on souhaiterait effectuer sur cette base des données. D'ailleurs elles seront codées plus tard pour ceux et celles qui voudraient venir en voir plus.