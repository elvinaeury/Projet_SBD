# Description du dossier Django

Ce dossier contient tous les fichiers relatifs à l'utilisation de django dans le cadre de ce projet (parties ORM et framework)

* Environnement du projet django  : [*DjangoAviation*](https://github.com/elvinaeury/Projet_SBD/tree/master/Django/DjangoAviation)
* Nom de l'application qui servira d'interface utilisateur : [*appliweb*](https://github.com/elvinaeury/Projet_SBD/tree/master/Django/DjangoAviation/appliweb)

## Partie ORM
 
### Utilisation du SGBD postgres
Le paramétrage du projet a été fait et l'utilisation du SGBD actée (voir le fichier [DjangoAviation/settings.py](https://github.com/elvinaeury/Projet_SBD/blob/master/Django/DjangoAviation/DjangoAviation/settings.py))

### Création et ajustement du modèle de données pour Django
Le modèle relationnel tel que décrit dans  [modele_relationnel/description_du_modele_relationne_final.md](https://github.com/elvinaeury/Projet_SBD/blob/master/modele_relationnel/description_modele_relationnel_final.md) est donc matérialisé ici via les classes django définies dans le fichier [appliweb/models.py](https://github.com/elvinaeury/Projet_SBD/blob/master/Django/DjangoAviation/appliweb/models.py)
Comme pressenti auparavant, les données manquantes ont engendré certaines contraintes comme la duplication du champn date d'un type timestamp en deux champs date et time de type varchar. Comme déjà mentionné, en fonction des futurs besoins, il sera peut-être question de supprimer ces données manquantes pour utiliser le bon type ou de les mettre dans une table à part. Il n'en est pas encore question à ce stade.

### Chargement des données dans les tables ainsi créées 
Le peuplement de la base se fait en deux étapes :
- peuplement de la table airports : se fait avec [script_peuplement_airports2.py](https://github.com/elvinaeury/Projet_SBD/blob/master/Django/script_peuplement_aiports2.py)
- peuplement des autres tables : se fait avec [scrip_peuplement_incidents2.py](https://github.com/elvinaeury/Projet_SBD/blob/master/Django/script_peuplement_incidents2.py)
Les scripts ont été testés avec succès et le chargement des données sera fait bientôt sur le serveur postgres de l'université.


## Partie FrameWork 

Les prochaines étapes seront consancrées à la partie web de l'application qui fera office d'interface utilisateur. Les différentes évolutions seront consignées ici progressivement.

...