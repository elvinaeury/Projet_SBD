# Description du dossier nettoyage 

Ce dossier contient les fichiers de données nettoyées et ceux relatifs au processus de nettoyage :

* fichier [donnees_traitees.zip](#https://github.com/elvinaeury/Projet_SBD/blob/master/nettoyage/donnees_traitees.zip) : archive du dossier des données traitées
* dossier [donnees_traitees](#https://github.com/elvinaeury/Projet_SBD/tree/master/nettoyage/donnees_traitees) : contient tous les fichiers csv non compressés des données obtenues par web scrapping après leur nettoyage.
* fichier [nettoyage.ipynb](#https://github.com/elvinaeury/Projet_SBD/blob/master/nettoyage/nettoyage.ipynb) : ce notebook retrace les principales idées dévéloppées pour traiter ces données sur base des données d'une année type d'un ancien format du jeu de données mais avec plus détails
* fichier [nettoyage2.ipynb](#https://github.com/elvinaeury/Projet_SBD/blob/master/nettoyage/nettoyage2.ipynb) : pareil que le notebook précédent mais sur le format de notre dernier jeu de données brutes (avec moins de détails qui sont les mêmes que ceux du notebook précédent)
* fichier [nettoyage2_generalise.py](#https://github.com/elvinaeury/Projet_SBD/blob/master/nettoyage/nettoyage2_generalise.py) : généralise l'ensemble des opérations de nettoyage et de mise en forme développées dans le dernier notebook

Pour ce nettoyage, nous avons utilisés notamment pandas et les expressions régulières du module re de python